"""
OOP approach using Protocols.

`type TicketOrderingStrategy = Callable[...]` from the functional approach
can be used instead of a Protocol because of __call__ method.

`RandomOrderingStrategy` shows a parametrized strategy.
"""
import random
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from .ticket import SupportTicket


class TicketOrderingStrategy(Protocol):
    "Tickets ordering strategy protocol."
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        "Reorder tickets."
        ...


class FIFOOrderingStrategy:
    "Return tickets in FIFO order."
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        "Reorder tickets."
        return tickets.copy()


class FILOOrderingStrategy:
    "Return tickets in FILO order."
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        "Reorder tickets."
        return list(reversed(tickets))


@dataclass
class RandomOrderingStrategy:
    """
    Return tickets in random order.

    This class can be initialized with a seed parameter: `RandomOrderingStrategy(42)`
    """
    seed: int | None = None

    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        "Reorder tickets."
        random.seed(self.seed)
        return random.sample(tickets, len(tickets))


class BlackHoleStrategy(TicketOrderingStrategy):
    "Discard all tickets."
    def __call__(self, _tickets: list[SupportTicket]) -> list[SupportTicket]:
        "Reorder tickets."
        return []


# Abstract class (OOP) approach

# class TicketOrderingStrategy(ABC):
#     "Tickets ordering strategy base class."

#     @abstractmethod
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         "Reorder tickets."


# class FIFOOrderingStrategy(TicketOrderingStrategy):
#     "Return tickets in FIFO order."
#
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
#         new_list = tickets.copy()
#         random.shuffle(new_list)
#         return new_list


# class BlackHoleStrategy(TicketOrderingStrategy):
#     "Discard all tickets."

#     @override
#     def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
#         return []
