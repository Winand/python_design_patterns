from dataclasses import dataclass


@dataclass
class Account:
    "Bank account."
    name: str
    number: str
    balance: int = 0

    def deposit(self, amount: int) -> None:
        "Deposit money."
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        "Withdraw money."
        if amount > self.balance:
            msg = f"Insufficient funds ({self.balance}) in {self.name} account."
            raise ValueError(msg)
        self.balance -= amount
