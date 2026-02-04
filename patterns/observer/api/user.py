from ..lib.db import create_user, find_user  # noqa: TID252
from ..lib.stringtools import get_random_string  # noqa: TID252
from .event import post_event


def register_new_user(name: str, password: str, email: str) -> None:
    "Register a new user."
    # create an entry in the database
    user = create_user(name, password, email)

    post_event("user_registered", user)
    # # post a Slack message to sales department
    # post_slack_message(
    #     "sales",
    #     f"{user.name} has registered with email address {user.email}. "
    #     "Please spam this person.",
    # )
    # # send a welcome email
    # send_email(
    #     user.name,
    #     user.email,
    #     "Welcome",
    #     f"Thanks for registering, {user.name}!\nRegards, The DevNotes team",
    # )
    # # write server log
    # log(f"User registered with email address {user.email}")


def password_forgotten(email: str) -> None:
    "Generate a password reset code."
    # retrieve the user
    user = find_user(email)
    # generate a password reset code
    user.reset_code = get_random_string(16)

    post_event("user_password_forgotten", user)
    # # send a password reset message
    # send_email(
    #     user.name,
    #     user.email,
    #     "Reset your password",
    #     f"To reset your password, use this very secure code: {user.reset_code}.\n"
    #     "Regards, The DevNotes team",
    # )
    # # write server log
    # log(f"User with email address {user.email} requested a password reset")


def reset_password(code: str, email: str, password: str) -> None:
    "Reset user password using a reset code."
    # retrieve the user
    user = find_user(email)

    user.reset_password(code, password)
