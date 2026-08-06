"Customer support handling class."

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .strategies import TicketOrderingStrategy
    from .ticket import SupportTicket

log = logging.getLogger(__name__)


class CustomerSupport:
    "A customer support system."

    def __init__(self) -> None:
        "Initialize the customer support system."
        self.tickets: list[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket) -> None:
        "Create a new customer ticket."
        self.tickets.append(ticket)

    def process_tickets(self, order: TicketOrderingStrategy) -> None:
        "Process tickets with the given ordering strategy."
        ticket_list = order(self.tickets)

        if not ticket_list:
            log.info("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            ticket.process()

        # clear the tickets list after processing
        self.tickets = []
