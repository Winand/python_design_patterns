**Abstract Factory** pattern provides an interface for creating
a family of related objects. New families can be added using inheritance.

[In comparison](https://refactoring.guru/design-patterns/factory-comparison),
**Factory Method** pattern *typically* produces a single object per subclass.
**Simple Factory** coding idiom is implemented as a single function using if/else
statements or dictionary to decide which object to create, rather than using
inheritance. So it is *tightly coupled* to all the classes it instantiates.
