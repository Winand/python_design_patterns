from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .transaction import Transaction


@dataclass
class BankController:
    "Bank operations controller."
    undo_stack: list[Transaction] = field(default_factory=list)
    redo_stack: list[Transaction] = field(default_factory=list)

    def execute(self, transaction: Transaction) -> None:
        "Execute a transaction."
        transaction.execute()
        self.redo_stack.clear()
        self.undo_stack.append(transaction)

    def undo(self) -> None:
        "Undo an operation from an undo stack."
        if not self.undo_stack:
            return
        transaction = self.undo_stack.pop()
        transaction.undo()
        self.redo_stack.append(transaction)

    def redo(self) -> None:
        "Redo an operation from a redo stack."
        if not self.redo_stack:
            return
        transaction = self.redo_stack.pop()
        transaction.redo()
        self.undo_stack.append(transaction)
