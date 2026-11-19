"""Where mutable state lives: files locally, Postgres when deployed.

Everything the pipeline *changes* goes through here: pipeline state,
decisions, corrections, overrides, the partners' calendar, email feedback and
templates, the outbox and the inbox. Read-only inputs (thesis, applications,
dossiers, score cards) stay as files shipped with the code.

Keys are repo-relative paths (e.g. "data/pipeline/state.json"), so the two
backends hold the same layout.

- FileStore (default): reads and writes under the repo root (TRIAGE_ROOT).
- PgStore (DATABASE_URL set): one table `docs(key, body, updated_at)`. A key
  not yet in the table falls back to the file shipped with the deployment, so
  the first deploy starts from the repo's seed state, and `reset()` returns to it.
"""
from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from . import core


def key(path: Path | str) -> str:
    p = Path(path)
    if p.is_absolute() and p.is_relative_to(core.ROOT):
        p = p.relative_to(core.ROOT)
    return p.as_posix()  # a path outside the repo (tests) stays absolute


class FileStore:
    name = "files"

    def _p(self, k: str) -> Path:
        return core.ROOT / k

    def read_text(self, k: str) -> str | None:
        p = self._p(k)
        return p.read_text(encoding="utf-8") if p.exists() else None

    def write_text(self, k: str, text: str) -> None:
        p = self._p(k)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def append_text(self, k: str, text: str) -> None:
        p = self._p(k)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as f:
            f.write(text)

    def list_keys(self, prefix: str) -> list[str]:
        base = self._p(prefix)
        if not base.exists():
            return []
        return sorted(key(p) for p in base.rglob("*") if p.is_file())

    def delete_prefix(self, prefix: str) -> None:  # pragma: no cover - not used with files
        raise NotImplementedError


class PgStore:
    """Postgres via Neon's SQL-over-HTTPS endpoint (what Neon's serverless
    driver uses): no socket to keep open, which suits short-lived functions."""

    name = "postgres"

    def __init__(self, url: str):
        self.url = url
        self.endpoint = f"https://{urlparse(url).hostname}/sql"

    def _run(self, sql: str, *params) -> list[list]:
        import requests

        r = requests.post(self.endpoint, json={"query": sql, "params": list(params)}, timeout=30, headers={
            "Neon-Connection-String": self.url, "Neon-Raw-Text-Output": "true", "Neon-Array-Mode": "true"})
        if r.status_code != 200:
            raise RuntimeError(f"database error {r.status_code}: {r.text[:300]}")
        return r.json().get("rows", [])

    def ensure(self) -> None:
        self._run("CREATE TABLE IF NOT EXISTS docs (key text PRIMARY KEY, body text NOT NULL, "
                  "updated_at timestamptz NOT NULL DEFAULT now())")

    def read_text(self, k: str) -> str | None:
        rows = self._run("SELECT body FROM docs WHERE key = $1", k)
        if rows:
            return rows[0][0]
        return FileStore().read_text(k)  # seed shipped with the deployment

    def write_text(self, k: str, text: str) -> None:
        self._run("INSERT INTO docs (key, body) VALUES ($1, $2) ON CONFLICT (key) DO UPDATE "
                  "SET body = EXCLUDED.body, updated_at = now()", k, text)

    def append_text(self, k: str, text: str) -> None:
        current = self.read_text(k) or ""
        self.write_text(k, current + text)

    def list_keys(self, prefix: str) -> list[str]:
        rows = self._run("SELECT key FROM docs WHERE key LIKE $1", prefix.rstrip("/") + "/%")
        return sorted(set(r[0] for r in rows) | set(FileStore().list_keys(prefix)))

    def delete_prefix(self, prefix: str) -> None:
        if prefix == "":
            self._run("DELETE FROM docs")
        else:
            self._run("DELETE FROM docs WHERE key LIKE $1", prefix.rstrip("/") + "/%")


@lru_cache(maxsize=1)
def store():
    url = os.environ.get("DATABASE_URL")
    return PgStore(url) if url else FileStore()


# ---------------------------------------------------------------- helpers

def read_text(path: Path | str) -> str | None:
    return store().read_text(key(path))


def write_text(path: Path | str, text: str) -> None:
    store().write_text(key(path), text)


def append_text(path: Path | str, text: str) -> None:
    store().append_text(key(path), text)


def exists(path: Path | str) -> bool:
    return read_text(path) is not None


def read_json(path: Path | str, default: Any = None) -> Any:
    t = read_text(path)
    return json.loads(t) if t is not None else default


def write_json(path: Path | str, obj: Any) -> None:
    if hasattr(obj, "model_dump"):
        obj = obj.model_dump(mode="json")
    write_text(path, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def list_keys(prefix: Path | str) -> list[str]:
    return store().list_keys(key(prefix))
