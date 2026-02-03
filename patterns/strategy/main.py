import logging
import random
import string
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from collections.abc import Callable

type TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)


def generate_id(length: int = 8) -> str:
    "Generate a random string of uppercase letters."
    return "".join(random.choices(string.ascii_uppercase, k=length))  # noqa: S311


# --- OOP approach ---
# class TicketOrderingStrategy(ABC):
#     "Tickets ordering strategy base class."

#     @abstractmethod
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         "Reorder tickets."


# class FIFOOrderingStrategy(TicketOrderingStrategy):
#     "Return tickets in FIFO order."

#     @override
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         return tickets.copy()


# class FILOOrderingStrategy(TicketOrderingStrategy):
#     "Return tickets in FILO order."

#     @override
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         return list(reversed(tickets))


# class RandomOrderingStrategy(TicketOrderingStrategy):
#     "Return tickets in random order."

#     @override
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         new_list = tickets
#         random.shuffle(new_list)
#         return new_list


# class BlackHoleStrategy(TicketOrderingStrategy):
#     "Discard all tickets."

#     @override
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         return []


# --- Functional approach ---
def fifo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    "Return tickets in FIFO order."
    return tickets.copy()


def filo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    "Return tickets in FILO order."
    return list(reversed(tickets))


def random_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    "Return tickets in random order."
    new_list = tickets
    random.shuffle(new_list)
    return new_list


def blackhole_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:  # noqa: ARG001
    "Discard all tickets."
    return []


@dataclass
class SupportTicket:
    "A customer support ticket."

    customer: str
    issue: str
    id: str = field(default_factory=generate_id)


class CustomerSupport:
    "A customer support system."

    tickets: ClassVar[list[SupportTicket]] = []

    def create_ticket(self, customer: str, issue: str) -> None:
        "Create a new customer ticket."
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, order: TicketOrderingStrategy) -> None:
        "Process tickets with the given ordering strategy."
        ticket_list = order(self.tickets)

        if not ticket_list:
            log.info("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket) -> None:
        "Process a single ticket."
        print(f"Processing ticket {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("-----")


def main() -> None:
    "Strategy pattern example."
    print("Hello from strategy!")
    print()

    app = CustomerSupport()

    # register tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VS Code doesn't solve my bugs on its own.")

    # process tickets
    app.process_tickets(filo_ordering)


if __name__ == "__main__":
    main()
