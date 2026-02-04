from typing import TYPE_CHECKING

from ..lib.email import send_email  # noqa: TID252
from .event import subscribe

if TYPE_CHECKING:
    from ..lib.db import User  # noqa: TID252


def handle_user_registered_event(user: User) -> None:
    "Send a welcome email."
    send_email(
        user.name,
        user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, The DevNotes team",
    )


def handle_user_password_forgotten_event(user: User) -> None:
    "Send a password reset message."
    send_email(
        user.name,
        user.email,
        "Reset your password",
        f"To reset your password, use this very secure code: {user.reset_code}.\n"
        "Regards, The DevNotes team",
    )


def handle_user_upgrade_plan_event(user: User) -> None:
    "Send a thank you email."
    send_email(
        user.name,
        user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it.\n"
        "Regards, The DevNotes team",
    )


def setup_email_event_handlers() -> None:
    "Subscribe to events."
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
