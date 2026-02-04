from .api.email_listener import setup_email_event_handlers
from .api.log_listener import setup_log_event_handlers
from .api.plan import upgrade_plan
from .api.slack_listener import setup_slack_event_handlers
from .api.user import password_forgotten, register_new_user


def main():
    print("Hello from observer!")

    # register event listeners
    setup_slack_event_handlers()
    setup_log_event_handlers()
    setup_email_event_handlers()

    # register a new user
    print("\n--- REGISTER NEW USER ---")
    register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

    # send a password reset message
    print("\n--- REQUEST PASSWORD RESET ---")
    password_forgotten("hi@arjanegges.com")

    # upgrade plan
    print("\n---UPGRADE USER PLAN ---")
    upgrade_plan("hi@arjanegges.com")


if __name__ == "__main__":
    main()
