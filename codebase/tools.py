"""Read-only order and policy lookups, deterministic limits, and draft actions."""

import json
from pathlib import Path

from tracing import tool

ROOT = Path(__file__).resolve().parents[1]


@tool
def get_order(order_id: str):
    """get_order · input: order ID · output: order or None · no external effect."""
    with (ROOT / "data/orders.json").open(encoding="utf-8") as file:
        return next((order for order in json.load(file) if order["order_id"] == order_id), None)


@tool
def get_policy(issue_type: str):
    """get_policy · input: issue type · output: policy code and text · no external effect."""
    code = {"missing_item": "CS-01", "late_delivery": "CS-02"}.get(issue_type, "CS-04")
    text = (ROOT / "data/policy.md").read_text(encoding="utf-8")
    return {"code": code, "text": next(line for line in text.splitlines() if line.startswith(f"- {code}:"))}


@tool
def check_limit(issue_type: str, amount: float, order: dict, item_price: float = 0):
    """check_limit · input: issue, amount, order, item price · output: limit verdict · no external effect."""
    if issue_type == "missing_item":
        allowed = item_price <= 10 and item_price <= round(order["total"] * 0.30, 2) and amount == item_price
        return {"allowed": allowed, "max_amount": min(10, round(order["total"] * 0.30, 2)), "policy_code": "CS-01"}
    if issue_type == "late_delivery":
        delay = order["delay_minutes"]
        maximum = 0 if delay < 15 else 2 if delay <= 30 else 5
        return {"allowed": amount == maximum, "max_amount": maximum, "policy_code": "CS-02"}
    return {"allowed": False, "max_amount": 0, "policy_code": "CS-04"}


@tool
def create_refund_draft(order_id: str, kind: str, amount: float, policy_code: str):
    """create_refund_draft · input: order, kind, amount, policy · output: approval draft · external effect: draft only."""
    return {"draft_id": f"DRAFT-{order_id}-{kind}", "status": "cho_duyet", "kind": kind, "amount": amount, "policy_code": policy_code}


@tool
def escalate_ticket(order_id: str, reason: str, policy_code: str):
    """escalate_ticket · input: order, reason, policy · output: handoff draft · external effect: draft only."""
    return {"ticket_id": f"TICKET-{order_id or 'UNKNOWN'}", "status": "cho_nhan_vien", "reason": reason, "policy_code": policy_code}
