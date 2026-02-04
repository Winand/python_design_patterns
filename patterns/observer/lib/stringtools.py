from random import choice
from string import ascii_lowercase


def get_random_string(length: int) -> str:
    "Generate a random string of lowercase letters of the specified length."
    return "".join(choice(ascii_lowercase) for i in range(length))  # noqa: S311
