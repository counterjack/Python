Reference:
https://refactoring.guru/design-patterns



                                Design Pattern
    __________________________________|___________________________________
    |                                 |                                  |
    Creational                      Behavioural                         Structural

    |_  Factory
    |_  Abstact Factory                                                 |_ Decorator
    |_  Singleton                   |_ Strategy                         |_ Adaptor
    |_  Builder                     |_ Observer                         |_ Bridge
    |_  Prototype                   |_ Iterator                         |_ Composite
                                    |_ Chain of Responsibility          |_ Facade
                                    |_ Command                          |_ Proxy
                                    |_ State                            |_ Fly Weight
                                    |_ Visitor
                                    |_ Momento
                                    |_ Mediator


### Factory :

Define an interface to create object but defer object instantiation at run time. 
Usage: Django test Factory methods

- When to use:
    -- Consider a scenario when you have base vehicle class. And presently, You only have cabs (4wheeler). 
    So most of your code will be tightly coupled with say `Cab` class. But in future, you want to introduce
    2 wheeler taxi (say BikeTaxi) then you have to change your entire code base. Better, Use a VehicleFactory class
    over the Vehicle Base class and use that VehicleFactory class to instantiate a new vehicle. 

### Singleton
Allow only one object to create
Usage: Logger, Terminal, DB Connection


### Builder
Helps in building complex logic using simple objects. It builds the final object step by step


## Strategy
Used in various frameworks to provide users a way to change the behaviour of a class without extending. 

## Chain of Responsibility

This design patterns allows passing request along the chain of potential handlers until one of them handles request

Ref: https://refactoring.guru/design-patterns/chain-of-responsibility/python/example

Pros:
- Flexibility on making the chain of handlers
- Each handler is responsible for it's own responsibility. i.e no dependancy and self contained

Cons
- there may be some requests which may not be processed by any handler


## Command


## Decorator