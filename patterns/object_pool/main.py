from contextlib import contextmanager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


@contextmanager
def pool_manager(pool: ReusablePool) -> Generator[Reusable]:
    "Aquire and release an object automatically."
    obj = pool.aquire()
    yield obj
    pool.release(obj)


class Reusable:
    "A reusable object."

    def test(self) -> None:
        "Print out current object id."
        print(f"Using object {id(self)}")


class PoolExhaustedError(Exception):
    "No more free objects in the pool."


class ReusablePool:
    "Reusable objects pool."

    def __init__(self, size: int) -> None:
        "Create a pool of Reusable objects with a given size."
        self.size = size
        self.free = []
        self.in_use = []
        for _ in range(size):
            self.free.append(Reusable())

    def aquire(self) -> Reusable:
        "Aquire an object from the pool."
        if not self.free:
            msg = "No more objects available"
            raise PoolExhaustedError(msg)
        r = self.free.pop()  # stack
        self.in_use.append(r)
        return r

    def release(self, r: Reusable) -> None:
        "Release an object back to the pool."
        self.in_use.remove(r)
        self.free.append(r)


def main() -> None:
    "Object pool pattern."
    print("Hello from object-pool!")
    pool = ReusablePool(size=2)
    with pool_manager(pool) as r:
        r.test()
    r = pool.aquire()
    r2 = pool.aquire()
    r.test()
    r2.test()

    pool.release(r2)
    r3 = pool.aquire()
    r3.test()


if __name__ == "__main__":
    main()
