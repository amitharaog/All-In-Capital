"""PDF -> markdown text for new applications (decks and form exports)."""
from __future__ import annotations

from pathlib import Path


def pdf_to_markdown(path: str) -> str:
    import pdfplumber

    parts = [f"<!-- source: {Path(path).name} (pdfplumber extraction) -->"]
    with pdfplumber.open(path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            text = (page.extract_text() or "").strip()
            parts.append(f"\n## Page {i}\n\n{text}")
            for t in page.extract_tables() or []:
                rows = [[(c or "").replace("\n", " ") for c in r] for r in t if r]
                if rows:
                    parts.append("| " + " | ".join(rows[0]) + " |\n|" + "---|" * len(rows[0]))
                    parts += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(parts) + "\n"
