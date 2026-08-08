from typing import Protocol


class Transaction(Protocol):
    "Transaction protocol."

    def execute(self) -> None:
        "Execute a transaction."
        ...
