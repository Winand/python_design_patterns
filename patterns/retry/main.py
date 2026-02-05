import json
import logging
import random
import time
from functools import wraps
from pathlib import Path
from typing import TYPE_CHECKING, Any

import httpx
import ollama

if TYPE_CHECKING:
    from collections.abc import Callable

logging.basicConfig(level="DEBUG")
logging.getLogger("httpcore").setLevel("INFO")
logging.getLogger("httpx").setLevel("WARNING")
log = logging.getLogger(__name__)


def retry_decorator(
    attempts: int = 3,  # number of attempts
    delay: float = 1,  # base delay time in seconds
    backoff_factor: float = 2,  # exponential delay: factor^(attempt-1)
    jitter: float = 0.1,  # delay offset factor
    default: Callable[..., Any] | None = None,  # (func types not available yet)
):
    "Call a function until success or max attempts reached."

    def decorator[T, **P](func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    log.warning("Attempt %s failed: %s", attempt, e)
                    if attempt == attempts:
                        if default:
                            return default(*args, **kwargs)
                        raise
                    # exponential backoff (s) with jitter (+/-%)
                    jitter_offset = random.uniform(-jitter, jitter)  # noqa: S311
                    sleep_time = (
                        delay * (backoff_factor ** (attempt - 1)) * (1 + jitter_offset)
                    )
                    log.debug("Waiting for %.1fs...", sleep_time)
                    time.sleep(sleep_time)
            msg = "Set a positive integer for retries"
            raise ValueError(msg)

        return wrapper

    return decorator


def retry[T](
    *funcs: Callable[[], T],
    delay: float = 1,  # base delay time in seconds
    backoff_factor: float = 2,  # exponential delay: factor^(attempt-1)
    jitter: float = 0.1,  # delay offset factor
) -> T:
    "Call functions from the list one by one until success."
    for attempt, func in enumerate(funcs, start=1):
        try:
            return func()
        except Exception as e:  # noqa: BLE001
            log.warning("Attempt %s failed: %s", attempt, e)
            # exponential backoff with jitter
            jitter_offset = random.uniform(-jitter, jitter)  # noqa: S311
            sleep_time = delay * (backoff_factor ** (attempt - 1)) * (1 + jitter_offset)
            log.debug("Waiting for %.1fs...", sleep_time)
            time.sleep(sleep_time)
    msg = "Retries have failed"
    raise RuntimeError(msg)


def fetch_joke() -> str:
    "Fetch a random joke from icanhazdadjoke.com."
    proxy_file = Path(__file__).parent / "proxy.txt"
    proxy = proxy_file.read_text().strip() if proxy_file.is_file() else None
    if random.random() < 0.85:  # noqa: PLR2004, S311
        proxy = None  # by turning proxy on/off we can trigger an error
    with httpx.Client(proxy=proxy) as client:
        response = client.get(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"},
        )
        response.raise_for_status()
        return response.json()["joke"]


@retry_decorator(backoff_factor=1, default=lambda _: "Can't get hobby")
def get_user_interest(text: str) -> str:
    "Get a user hobby from a text string using Qwen2.5-coder LLM."
    response = ollama.generate(
        model="qwen2.5-coder:1.5b",
        prompt=f"Extract the user info with a hobby or hobbies from this text: {text}",
        format="json",
    )
    content = response["response"]
    return json.loads(content)["hobby"]


def main() -> None:
    "Retry pattern."
    print("Hello from retry!")

    print("\n--- icanhazdadjoke ---")
    joke = retry(*[fetch_joke] * 2, lambda: "No joke available")
    print(joke)

    print("\n--- LLM ---")
    text = "Hi, my name is Alice and I'm 30 years old. I like fishing."
    print(get_user_interest(text))


if __name__ == "__main__":
    main()
