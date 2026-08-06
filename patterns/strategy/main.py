import logging

from .support.app import CustomerSupport
from .support.strategies import random_strategy_creator
from .support.ticket import SupportTicket

logging.basicConfig(level="INFO")


def main() -> None:
    "Strategy pattern example."
    print("Hello from strategy!")
    print()

    app = CustomerSupport()

    # register tickets
    app.add_ticket(
        SupportTicket("John Smith", "My computer makes strange sounds!"),
    )
    app.add_ticket(
        SupportTicket("Linus Sebastian", "I can't upload any videos, please help."),
    )
    app.add_ticket(
        SupportTicket("Arjan Egges", "VS Code doesn't solve my bugs on its own."),
    )

    # process tickets
    app.process_tickets(random_strategy_creator(seed=5))


if __name__ == "__main__":
    main()
