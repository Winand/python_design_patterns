import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .transaction import Transaction

if TYPE_CHECKING:
    from .account import Account

log = logging.getLogger(__name__)


@dataclass
class Deposit:
    "Deposit operation."
    amount: int
    account: Account

    @property
    def transaction_details(self) -> str:
        "Transaction details text."
        return f"${self.amount / 100:.2f} to account {self.account.name}"

    def execute(self) -> None:
        "Execute a deposit operation."
        self.account.deposit(self.amount)
        log.info("Deposited %s", self.transaction_details)

    def undo(self) -> None:
        "Undo deposit operation."
        self.account.withdraw(self.amount)
        log.info("Undid deposit of %s", self.transaction_details)

    def redo(self) -> None:
        "Undo deposit operation."
        self.account.deposit(self.amount)
        log.info("Redid deposit of %s", self.transaction_details)


@dataclass
class Withdrawal:
    "Withdrawal operation."
    amount: int
    account: Account

    @property
    def transaction_details(self) -> str:
        "Transaction details text."
        return f"${self.amount / 100:.2f} from account {self.account.name}"

    def execute(self) -> None:
        "Execute a Withdrawal operation."
        self.account.withdraw(self.amount)
        log.info("Withdrawn %s", self.transaction_details)

    def undo(self) -> None:
        "Undo deposit operation."
        self.account.deposit(self.amount)
        log.info("Undid withdrawal of %s", self.transaction_details)

    def redo(self) -> None:
        "Undo deposit operation."
        self.account.withdraw(self.amount)
        log.info("Redid withdrawal of %s", self.transaction_details)


@dataclass
class Transfer:
    "Money transfer operation."
    amount: int
    from_account: Account
    to_account: Account

    @property
    def transaction_details(self) -> str:
        "Transaction details text."
        return (f"${self.amount / 100:.2f} from account {self.from_account.name} "
                f"to account {self.to_account.name}")

    def execute(self) -> None:
        "Execute a money transfer operation."
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        log.info("Transfered %s", self.transaction_details)

    def undo(self) -> None:
        "Undo deposit operation."
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)
        log.info("Undid transfer of %s", self.transaction_details)

    def redo(self) -> None:
        "Undo deposit operation."
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        log.info("Redid transfer of %s", self.transaction_details)


@dataclass
class Batch:
    "Batch of operations."
    commands: list[Transaction] = field(default_factory=list)

    def execute(self) -> None:
        "Execute multiple operations as a single transaction."
        completed_commands: list[Transaction] = []
        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)
        except ValueError:
            log.exception("Batch command failed")
            for command in reversed(completed_commands):
                command.undo()

    def undo(self) -> None:
        "Undo all of the operations."
        # NOTE: exceptions are not handled https://youtu.be/FM71_a3txTo?t=1591
        for command in reversed(self.commands):
            command.undo()

    def redo(self) -> None:
        "Redo all of the operations."
        for command in reversed(self.commands):
            command.redo()
