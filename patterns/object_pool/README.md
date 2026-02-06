# Object Pool Pattern
**Object pool** is used to manage a collection of reusable objects instead of creating
new ones. It is useful when creating a new object is expensive and it is needed
only for a short period of time, e.g. a database connection. Pool manager is also
responsible for cleaning up objects before they are returned to the pool.

In comparison, [Singleton](../singleton/README.md) pattern is used to ensure a
class has only one instance.
