"""Draft Email -> HITL -> Send Email, and the inbox the booking agent reads.

Whiteboard boxes covered here:
- Draft Email: from a template in data/fund/email_templates/<kind>.txt.
- HITL + feedback loop: a reviewer approves or edits each first email. An
  edit is logged in data/fund/email_feedback.jsonl, and with --save-template
  the edited email is generalised back into the template (company, founder,
  partners and slot lines become placeholders), so the next draft starts
  from the reviewer's version.
- Send Email: OutboxBackend (default) writes real RFC 822 .eml files to
  runs/outbox/; SMTPBackend sends them (set EMAIL_BACKEND=smtp and SMTP_*).
- Inbox: LocalInbox reads founder replies dropped in data/pipeline/inbox/<slug>/;
  IMAPInbox reads a real mailbox (INBOX_BACKEND=imap and IMAP_*). Replies are
  matched to the application by the reference tag in the subject.
"""
from __future__ import annotations

import datetime as dt
import email
import email.policy
import json
import os
import re
from email.message import EmailMessage
from pathlib import Path

from . import storage
from .core import DATA, FUND, ROOT

TEMPLATES = FUND / "email_templates"
FEEDBACK = FUND / "email_feedback.jsonl"
OUTBOX = ROOT / "runs" / "outbox"
INBOX = DATA / "pipeline" / "inbox"
FROM_ADDR = os.environ.get("EMAIL_FROM", "riya@allincapital.example")

DEFAULT_TEMPLATES = {
    "invite": (
        "Subject: All In Capital x {company}: 30 min intro call\n\n"
        "Hi {founder_first},\n\n"
        "Thanks for applying to All In Capital. {partners} would like to take a 30-minute call about {company}.\n"
        "We've held the first slot below for you. If it doesn't work, reply with another one from the list:\n\n"
        "{slot_lines}\n\n"
        "Just reply to this email with the slot that works.\n\n"
        "Best,\n{sender}\nAll In Capital\n"
    ),
    "followup": (
        "Subject: Re: All In Capital x {company}: 30 min intro call\n\n"
        "Hi {founder_first},\n\n"
        "Following up on our note from {days} days ago. We'd still like to talk about {company}. These slots are open:\n\n"
        "{slot_lines}\n\n"
        "A one-line reply with the slot that suits you is enough.\n\n"
        "Best,\n{sender}\nAll In Capital\n"
    ),
    "reschedule": (
        "Subject: Re: All In Capital x {company}: 30 min intro call\n\n"
        "Hi {founder_first},\n\n"
        "No problem. Here are some other times:\n\n"
        "{slot_lines}\n\n"
        "Reply with the one that works.\n\n"
        "Best,\n{sender}\nAll In Capital\n"
    ),
    "confirmation": (
        "Subject: Confirmed: All In Capital x {company}, {slot_human}\n\n"
        "Hi {founder_first},\n\n"
        "You're booked with {partners} on {slot_human} for 30 minutes. The calendar invite is attached.\n\n"
        "Best,\n{sender}\nAll In Capital\n"
    ),
    "pass": (
        "Subject: Your application to All In Capital: {company}\n\n"
        "Hi {founder_first},\n\n"
        "Thank you for sending us {company}. We're not going to take this forward right now, and we'd rather tell you why than go quiet.\n\n"
        "What would change our view: {what_would_change}\n\n"
        "If that changes, write back and we'll take another look.\n\n"
        "Best,\n{sender}\nAll In Capital\n"
    ),
}


def ref_tag(slug: str) -> str:
    return f"[AIC-{slug}]"


def template(kind: str) -> str:
    return storage.read_text(TEMPLATES / f"{kind}.txt") or DEFAULT_TEMPLATES[kind]


def human_slot(iso: str) -> str:
    s = dt.datetime.fromisoformat(iso)
    return s.strftime("%A %d %b, %I:%M %p") + " IST"


def slot_lines(slots: list[str]) -> str:
    return "\n".join(f"  {i}. {human_slot(s)}" for i, s in enumerate(slots, 1))


def render(kind: str, **values) -> dict:
    """Fill a template. Returns {subject, body}. The reference tag is always
    appended to the subject so replies can be matched."""
    values.setdefault("sender", "Riya")
    if "slots" in values:
        values["slot_lines"] = slot_lines(values.pop("slots"))
    text = template(kind).format_map(_Safe(values))
    subject, _, body = text.partition("\n\n")
    subject = subject.removeprefix("Subject: ").strip()
    if ref_tag(values["slug"]) not in subject:
        subject = f"{subject} {ref_tag(values['slug'])}"
    return {"subject": subject, "body": body.lstrip("\n")}


class _Safe(dict):
    def __missing__(self, key):
        return "{" + key + "}"


# --------------------------------------------------------------- feedback

def record_feedback(slug: str, kind: str, original: dict, edited: dict, note: str, by: str,
                    values: dict, save_template: bool) -> dict:
    entry = {
        "date": dt.date.today().isoformat(), "slug": slug, "kind": kind, "by": by, "note": note,
        "changed": original != edited, "saved_as_template": False,
    }
    if save_template and original != edited:
        storage.write_text(TEMPLATES / f"{kind}.txt", generalise(edited, values))
        entry["saved_as_template"] = True
    storage.append_text(FEEDBACK, json.dumps(entry) + "\n")
    return entry


def generalise(edited: dict, values: dict) -> str:
    """Turn a reviewer's edited email back into a template."""
    subject = edited["subject"].replace(ref_tag(values["slug"]), "").strip()
    text = f"Subject: {subject}\n\n{edited['body']}"
    if values.get("slots"):
        text = text.replace(slot_lines(values["slots"]), "{slot_lines}")
    for key in ("company", "partners", "founder_first", "sender"):
        if values.get(key):
            text = text.replace(values[key], "{" + key + "}")
    return text


def style_notes(kind: str, limit: int = 5) -> list[str]:
    notes = [json.loads(line) for line in (storage.read_text(FEEDBACK) or "").splitlines() if line.strip()]
    return [n["note"] for n in notes if n["kind"] == kind and n.get("note")][-limit:]


# --------------------------------------------------------------- send

def build_message(to: str | None, subject: str, body: str, ics: str | None = None,
                  in_reply_to: str | None = None) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = FROM_ADDR
    msg["To"] = to or "founder-address-missing@invalid"
    msg["Subject"] = subject
    msg["Date"] = email.utils.format_datetime(dt.datetime.now(dt.timezone.utc))
    msg["Message-ID"] = email.utils.make_msgid(domain="allincapital-triage")
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
        msg["References"] = in_reply_to
    msg.set_content(body)
    if ics:
        msg.add_attachment(ics.encode(), maintype="text", subtype="calendar", filename="invite.ics",
                           params={"method": "REQUEST"})
    return msg


class OutboxBackend:
    name = "outbox"

    def send(self, slug: str, kind: str, msg: EmailMessage) -> str:
        existing = [k for k in storage.list_keys(OUTBOX / slug) if k.endswith(".eml")]
        path = OUTBOX / slug / f"{len(existing) + 1:02d}_{kind}.eml"
        storage.write_text(path, msg.as_bytes(policy=email.policy.SMTP).decode("utf-8", "replace"))
        return storage.key(path)


class SMTPBackend:  # pragma: no cover - needs a mail server
    name = "smtp"

    def send(self, slug: str, kind: str, msg: EmailMessage) -> str:
        import smtplib

        with smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ.get("SMTP_PORT", "587"))) as s:
            s.starttls()
            s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
            s.send_message(msg)
        OutboxBackend().send(slug, kind, msg)  # keep a copy for the audit trail
        return msg["Message-ID"]


def sender():
    return SMTPBackend() if os.environ.get("EMAIL_BACKEND") == "smtp" else OutboxBackend()


# --------------------------------------------------------------- inbox

class LocalInbox:
    """Founder replies as .txt or .eml files in data/pipeline/inbox/<slug>/.
    Each file is read once (tracked in the pipeline state)."""

    name = "local"

    def fetch(self, slug: str, seen: set[str]) -> list[dict]:
        out = []
        for k in storage.list_keys(INBOX / slug):
            key = k.rsplit("/", 1)[-1]
            if key in seen or not key.endswith((".txt", ".eml")):
                continue
            raw = (storage.read_text(k) or "").encode("utf-8")
            if key.endswith(".eml"):
                m = email.message_from_bytes(raw, policy=email.policy.default)
                part = m.get_body(preferencelist=("plain",))
                body = part.get_content() if part else ""
                out.append({"id": key, "subject": m["Subject"] or "", "body": body, "from": m["From"] or ""})
            else:
                out.append({"id": key, "subject": "", "body": raw.decode("utf-8", "replace"), "from": ""})
        return out


class IMAPInbox:  # pragma: no cover - needs a mailbox
    name = "imap"

    def fetch(self, slug: str, seen: set[str]) -> list[dict]:
        import imaplib

        out = []
        with imaplib.IMAP4_SSL(os.environ["IMAP_HOST"]) as m:
            m.login(os.environ["IMAP_USER"], os.environ["IMAP_PASSWORD"])
            m.select("INBOX")
            _, data = m.search(None, f'(SUBJECT "{ref_tag(slug)}")')
            for num in data[0].split():
                _, msg_data = m.fetch(num, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1], policy=email.policy.default)
                key = msg["Message-ID"] or num.decode()
                if key in seen or (msg["From"] or "").endswith(FROM_ADDR):
                    continue
                part = msg.get_body(preferencelist=("plain",))
                out.append({"id": key, "subject": msg["Subject"] or "", "from": msg["From"] or "",
                            "body": part.get_content() if part else ""})
        return out


def inbox():
    return IMAPInbox() if os.environ.get("INBOX_BACKEND") == "imap" else LocalInbox()


def strip_quoted(body: str) -> str:
    """Keep only the founder's new text, not the quoted thread below it."""
    lines = []
    for line in body.splitlines():
        if line.startswith(">") or re.match(r"^On .+ wrote:$", line.strip()):
            break
        lines.append(line)
    return "\n".join(lines).strip()


def read_eml(path: Path) -> EmailMessage:
    return email.message_from_bytes(path.read_bytes(), policy=email.policy.default)
