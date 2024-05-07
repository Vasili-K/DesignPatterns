# Порождающие паттерны проектирования
### отвечают за удобное и безопасное создание новых объектов или даже целых семейств объектов.

### provide various object creation mechanisms, which increase flexibility and reuse of existing code.
[Refactoring Guru](https://refactoring.guru/ru/design-patterns/creational-patterns)

Эти паттерны увеличивают гибкость системы в процессе создания объектов, позволяя коду быть более обобщенным и не зависеть от конкретных классов объектов, которые необходимо создать.

These patterns help to make a system independent of how its objects are created, composed, and represented. They increase the system's flexibility in terms of object creation by enabling code to be more generalized and not dependent on the specific classes of objects that need to be created.

## Factory Method

#### это порождающий паттерн проектирования, который определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

#### is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.
[Refactoring Guru](https://refactoring.guru/ru/design-patterns/creational-patterns)

Основная идея паттерна заключается в том, чтобы делегировать создание экземпляров классов подклассам, что увеличивает гибкость и повторное использование кода.
