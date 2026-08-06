"""
Functional approach.

`random_strategy_creator` shows how to create a parametrized strategy using closures.
"""
import random
from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ticket import SupportTicket

type TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]


def fifo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    "Return tickets in FIFO order."
    return tickets.copy()


def filo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    "Return tickets in FILO order."
    return list(reversed(tickets))


def random_strategy_creator(seed: int | None = None) -> TicketOrderingStrategy:
    "Create random strategy with a seed parameter provided."
    def random_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
        "Return tickets in random order."
        # new_list = tickets.copy()
        # random.shuffle(new_list)
        # return new_list
        random.seed(seed)
        return random.sample(tickets, len(tickets))
    return random_ordering


def blackhole_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:  # noqa: ARG001
    "Discard all tickets."
    return []
