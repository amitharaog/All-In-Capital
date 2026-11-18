"""DEMO of the booking step. Not partner decisions.

Pretends Kushal accepted every suggestion in the latest batch (take the call ->
call, suggest pass -> pass; holds and screens get no action) and writes what
the booking step would produce to runs/<date>/demo_outbox/. The real outbox is
only ever written from data/decisions.json, which Kushal's approvals fill.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from triage.booking import book_approved  # noqa: E402
from triage.core import RUNS, load_json  # noqa: E402

batch = load_json(sorted(RUNS.glob("*/batch.json"))[-1])
mapping = {"TAKE_CALL": "call", "PASS": "pass", "HOLD_CONFLICT": "hold", "SCREEN_FIRST": "screen"}
demo = {
    i["dossier"]["slug"]: {"decision": mapping[i["verdict"]["recommendation"]], "by": "DEMO (mirrors system suggestion)"}
    for i in batch["items"]
}
print(json.dumps(book_approved(decisions=demo, outbox="demo_outbox"), indent=2))
