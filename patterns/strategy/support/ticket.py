import random
import string
from dataclasses import dataclass, field


def generate_id(length: int = 8) -> str:
    "Generate a random string of uppercase letters."
    return "".join(random.choices(string.ascii_uppercase, k=length))  # noqa: S311


@dataclass
class SupportTicket:
    "A customer support ticket."

    customer: str
    issue: str
    id: str = field(default_factory=generate_id, init=False)
    # id: str = field(init=False)

    # def __post_init__(self) -> None:
    #     "Generate a unique ID for the ticket."
    #     self.id = generate_id()

    def process(self) -> None:
        "Process this support ticket."
        print("===============================")
        print(f"Processing ticket id: {self.id}")
        print(f"Customer: {self.customer}")
        print(f"Issue: {self.issue}")
        print("===============================")
