"""Vercel entrypoint: Vercel detects the FastAPI `app` here."""
from triage.web import app  # noqa: F401
