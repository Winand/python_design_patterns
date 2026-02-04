from typing import TYPE_CHECKING

from ..lib.slack import post_slack_message  # noqa: TID252
from .event import subscribe

if TYPE_CHECKING:
    from ..lib.db import User  # noqa: TID252


def handle_user_registered_event(user: User) -> None:
    "Handle new user registration event."
    post_slack_message(
        "sales",
        f"{user.name} has registered with email address {user.email}. "
        "Don't forget to spam this person!",
    )


def handle_user_upgrade_plan_event(user: User) -> None:
    "Handle plan upgrade event."
    post_slack_message("sales", f"{user.name} has upgraded their plan.")


def setup_slack_event_handlers() -> None:
    "Subscribe to events."
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
