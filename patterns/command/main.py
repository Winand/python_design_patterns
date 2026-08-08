import logging

from .banking.bank import Bank
from .banking.commands import Batch, Deposit, Transfer, Withdrawal
from .banking.controller import BankController

logging.basicConfig(level="INFO")


def main() -> None:
    "Command pattern example."
    print("Hello from command!")

    # create a bank
    bank = Bank()

    # create a bank controller
    controller = BankController()

    # create some accounts
    account1 = bank.create_account("ArjanCodes")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    controller.execute(Deposit(100000, account1))

    controller.execute(Batch(commands=[
        Deposit(100000, account2),
        Deposit(100000, account3),
        # Withdrawal(10000000, account3),
        Transfer(50000, from_account=account2, to_account=account1),
    ]))

    # controller.execute(Withdrawal(150000, account1))
    # controller.undo()

    print(bank)


if __name__ == "__main__":
    main()
