import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .account import Account
    from .transaction import Transaction

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


@dataclass
class Batch:
    "Batch of operations."
    commands: list[Transaction] = field(default_factory=list)

    def execute(self) -> None:
        "Execute multiple operations as a single transaction."
        for command in self.commands:
            command.execute()
