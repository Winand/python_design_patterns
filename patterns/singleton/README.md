# Singleton Anti-Pattern
**Singleton** is a design pattern where a class can only have one instance.
This pattern can be replaced with a Python module, because modules are singletons
by themselves.

Singleton is considered an [anti-pattern](https://www.michaelsafyan.com/tech/design/patterns/singleton)
in many cases. Development becomes less flexible when we assume that a class will
always be instantiated only once. Singleton pattern is difficult to implement
correctly in multi-threaded applications due to possible race conditions.
Testing is difficult too because you cannot get a fresh instance in each test.
Also you can bypass single instance limitation by using e.g. inheritance.

On the other hand it is possible to separate business logic from the singleton
and use it directly in tests, but wrap it into a thread-safe (or not) singleton
in production code.

In comparison, [Object Pool pattern](../object_pool/README.md) is used to manage
a limited number of instances. But the pool itself can be implemented as a singleton.
