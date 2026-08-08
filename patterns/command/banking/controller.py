from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .transaction import Transaction


@dataclass
class BankController:
    "Bank operations controller."
    ledger: list[Transaction] = field(default_factory=list)
    next_item: int = 0

    def register(self, transaction: Transaction) -> None:
        "Register a transaction in the ledger."
        del self.ledger[self.next_item:]  # drop available redo actions
        self.ledger.append(transaction)
        self.next_item += 1

    def undo(self) -> None:
        "Undo an operation in the ledger."
        if self.next_item > 0:
            self.next_item -= 1

    def redo(self) -> None:
        "Redo an operation in the ledger."
        if self.next_item < len(self.ledger):
            self.next_item += 1

    def compute_balances(self) -> None:
        "Materialize current balances by replaying the ledger history."
        for transaction in self.ledger[:self.next_item]:
            transaction.execute()
