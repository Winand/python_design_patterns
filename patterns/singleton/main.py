from typing import Any, ClassVar


class Singleton(type):
    "Singleton metaclass."

    _instances: ClassVar[dict[type, Any]] = {}

    def __call__(cls, *args, **kwargs) -> Any:  # noqa: ANN002, ANN003, ANN401
        "Create a new instance or return the existing one."
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    "Singleton logger class."

    def log(self, msg: str) -> None:
        "Log a message."
        print("LOG:", msg)


def main() -> None:
    "Singleton pattern."
    print("Hello from singleton!")

    logger = Logger()
    logger2 = Logger()

    print("Same logger object:", logger is logger2)

    logger.log("Hello, world!")
    logger2.log("Hello, world!")


if __name__ == "__main__":
    main()
