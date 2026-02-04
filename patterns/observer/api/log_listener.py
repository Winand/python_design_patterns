from typing import TYPE_CHECKING

from ..lib.log import log  # noqa: TID252
from .event import subscribe

if TYPE_CHECKING:
    from ..lib.db import User  # noqa: TID252


def handle_user_registered_event(user: User) -> None:
    "Handle new user registration event."
    log(f"User registered with email address {user.email}")


def handle_user_password_forgotten_event(user: User) -> None:
    "Handle password reset request event."
    log(f"User with email address {user.email} requested a password reset")


def handle_user_upgrade_plan_event(user: User) -> None:
    "Handle plan upgrade event."
    log(f"User with email address {user.email} has upgraded their plan")


def setup_log_event_handlers() -> None:
    "Subscribe to events."
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
