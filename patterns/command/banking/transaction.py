from typing import Protocol


class Transaction(Protocol):
    "Transaction protocol."

    def execute(self) -> None:
        "Execute a transaction."
        ...

    def undo(self) -> None:
        "Undo an operation."
        ...

    def redo(self) -> None:
        "Redo an operation."
        ...
