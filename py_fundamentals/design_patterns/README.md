# Design Patterns with Python

This project is about classics software design patterns and how they can be implemented in Python.

---

## Lazy Initialization

<div style="background-color:#E8D6BE; text-align: center;">
  <img width="300px" src="https://littleauthors.in/wp-content/uploads/2022/09/lazyman.jpg">
</div>

Lazy initialization is a technique in object-oriented programming (OOP) that delays the creation of an object or the calculation of a value until the first time it is needed. It can improve the performance and memory efficiency of your code, but it also has some potential pitfalls. In this article, you will learn about the benefits and drawbacks of lazy initialization in OOP, and how to apply it wisely.

> It is used to increase application performance, speed up the initialization process, and reduces resource consumption: bandwidth, database load, RAM, and CPU usage.

**What is lazy initialization?** Lazy initialization is based on the idea of avoiding unnecessary work. Instead of initializing an object or a value at the time of declaration, you can defer it until the point of use. This way, you can save memory and processing time, and avoid errors or exceptions that might occur during initialization. For example, suppose you have a class that represents a database connection. You can use lazy initialization to create the connection only when you need to execute a query, rather than when you instantiate the class. This can reduce the overhead of opening and closing connections, and handle the possibility of connection failures.

**How to implement lazy initialization?** Implementing lazy initialization in OOP can be done in various ways, depending on the language and design pattern used. For instance, in Java a private static variable can be used to hold a singleton instance, and this variable is assigned to null initially. A synchronized method can then be used to check if the variable is null and create the instance if necessary.

**What are the benefits of lazy initialization?** Lazy initialization can offer several advantages for your OOP code, such as improved performance and memory efficiency by only creating objects or values when needed. It can also simplify the code by separating the declaration and initialization of objects or values, and enhance the modularity and flexibility of the code by allowing objects or values to be initialized dynamically. Additionally, lazy initialization can help handle errors or exceptions gracefully by delaying the initialization until the point of use.

**What are the drawbacks of lazy initialization?** Lazy initialization can have some drawbacks for your OOP code, such as introducing complexity and overhead by requiring additional checks or wrappers for objects or values, and managing their state and synchronization. It can also reduce readability and maintainability by hiding the initialization logic or parameters from the declaration, making the code less explicit or predictable. Furthermore, it can lead to unexpected behavior or bugs by violating the principle of least surprise, creating dependencies or side effects between objects or values. Lastly, it can negatively affect performance or memory efficiency by creating objects or values too late, wasting resources or time.

**How to use lazy initialization wisely?** Lazy initialization can be a useful technique for optimizing your OOP code, but it is not a silver bullet and should be used carefully. When deciding when to use it, consider whether the objects or values are expensive to create or rarely used. It is important to choose the appropriate implementation method for your language and design pattern, as well as use built-in or standard features or libraries if available. Make sure to document and test your code thoroughly and ensure that the initialization logic and parameters are clear and consistent. Additionally, avoid using lazy initialization for objects or values that have side effects or dependencies, which could affect the state or behavior of other objects or values. Finally, monitor and measure the performance and memory efficiency of your code, and compare it with alternative solutions.

<p style="text-align: right;">based on <a href='https://www.linkedin.com/advice/0/what-benefits-drawbacks-lazy-initialization' target=blank>what-benefits-drawbacks-lazy-initialization<a><p>

---

## GoF

### Creational Design Patterns

#### Abstract Factory Pattern
:cyclone:

#### Builder Pattern
:snake:

#### Factory Pattern
:turtle:

#### Prototype Pattern
:octocat:

#### Singleton Pattern

### Structural Design Patterns

#### Adapter
#### Bridge
#### Composite
#### Decorator
#### Facade
#### Flyweight
#### Proxy

### Behavioral Design Patterns

#### Chain of Responsibility
#### Command
#### Iterator
#### Mediator
#### Memento
#### Observer
#### State
#### Strategy
#### Template Method
#### Visitor
