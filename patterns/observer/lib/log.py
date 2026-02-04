from datetime import datetime


def log(msg: str) -> None:
    print(f"{datetime.now().astimezone()} - {msg}")
