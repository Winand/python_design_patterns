# Abstract Factory Pattern
**Abstract Factory** pattern provides an interface for creating
a family of related objects. New families can be added using inheritance.

[In comparison](https://refactoring.guru/design-patterns/factory-comparison),
**Factory Method** pattern *typically* produces a single object per subclass.
**Simple Factory** coding idiom is implemented as a single function using if/else
statements or dictionary to decide which object to create, rather than using
inheritance. So it is *tightly coupled* to all the classes it instantiates.

## Using Protocols
*An alternative implementation of Abstract Factory based on protocols is available
in `main_protocols.py` file.*

In Python *protocols* can be used as a more flexible alternative to inheritance.
Basically, protocols define an interface which should be implemented by classes
to be considered compatible with it via *duck typing*.

A class does not need to inherit from a protocol directly. Though protocols can
be used as a drop-in replacement for inheritance because a class can inherit
from a protocol and `@abstractmethod`, `@override` decorators can be used too.

Normally protocols have only method headers like `def name(self) -> None: ...`,
but they can also have method implementations like *abstract classes* do.
And like *abstract classes* a protocol cannot be instantiated directly,
but it can contain all the methods which implement this protocol. Then any class
which inherits from the protocol will already implement it.

While a protocol requires `@runtime_checkable` decorator for `isinstance`,
`issubclass` checks at runtime, it is not required for static type checkers like
mypy, pyright, etc. At design time they can check compatibility based on method
signatures only.
