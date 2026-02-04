from ..lib.db import find_user  # noqa: TID252
from .event import post_event


def upgrade_plan(email: str) -> None:
    "Upgrade user's plan to paid."
    user = find_user(email)
    user.plan = "paid"
    post_event("user_upgrade_plan", user)
