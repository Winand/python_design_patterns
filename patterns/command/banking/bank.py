import random
import string
from dataclasses import dataclass, field

from .account import Account


@dataclass
class Bank:
    "Bank management class."
    accounts: dict[str, Account] = field(default_factory=dict)

    def create_account(self, name: str) -> Account:
        "Create a new bank account with a specified name."
        number = "".join(random.choices(string.digits, k=12))  # noqa: S311
        account = Account(name, number)
        self.accounts[number] = account
        return account

    def get_account(self, account_number: str) -> Account:
        "Get an existing bank account by its number."
        return self.accounts[account_number]
