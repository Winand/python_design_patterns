from dataclasses import dataclass, field


@dataclass
class Account:
    "Bank account."
    name: str
    number: str
    _balance_cache: int = field(default=0, init=False)

    def deposit(self, amount: int) -> None:
        "Deposit money."
        self._balance_cache += amount

    def withdraw(self, amount: int) -> None:
        "Withdraw money."
        if amount > self._balance_cache:
            msg = f"Insufficient funds ({self._balance_cache}) in {self.name} account."
            raise ValueError(msg)
        self._balance_cache -= amount

    def clear_cache(self) -> None:
        "Clear cached balance value."
        self._balance_cache = 0
