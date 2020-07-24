Reference:
https://refactoring.guru/design-patterns



                                Design Pattern
    __________________________________|___________________________________
    |                                 |                                  |
    Creational                      Behavioural                         Structural

    |_  Factory
    |_  Abstact Factory             |_ Template Method                  |_ Decorator
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

Ref: https://refactoring.guru/design-patterns/builder/python/example


## Strategy
Used in various frameworks to provide users a way to change the behaviour of a class without extending. 
Eg: Various Payment modes, Different types of notification to users (email/message/sms)


## Chain of Responsibility

This design patterns allows passing request along the chain of potential handlers until one of them handles request

Ref: https://refactoring.guru/design-patterns/chain-of-responsibility/python/example

Pros:
- Flexibility on making the chain of handlers
- Each handler is responsible for it's own responsibility. i.e no dependancy and self contained

Cons
- there may be some requests which may not be processed by any handler


## Command
Ref: https://refactoring.guru/design-patterns/command

- When to use
The conversion allows deferred or remote execution of commands, storing command history, etc.


Provides a clear separation between client and server by bringing the concept
of sender and receiver.

Eg: Email Abstract Command Implementation

## Decorator (TODO)

Ref: https://refactoring.guru/design-patterns/decorator/python/example


## Iterator
Ref: https://refactoring.guru/design-patterns/iterator

- Allow traverse on the set of elements without exposing it's underlying representation.

Why ?
- The main idea of the Iterator pattern is to extract the traversal behavior of a collection
 into a separate object called an iterator.
 
 ## Observer
 Ref: https://refactoring.guru/design-patterns/observer/python/example
 

 The Observer pattern provides a way to subscribe and unsubscribe to and from these events 
 for any object that implements a subscriber interface.
 
 Eg: Notifying user for some events, stock market updates
 
 
 ## Template Method
 Ref: https://refactoring.guru/design-patterns/template-method
 
 - Template Method is a behavioral design pattern that defines the skeleton of an algorithm 
 in the superclass but lets subclasses override specific steps of the algorithm without 
 changing its structure.
 
 Eg: Data Mining process on various doc formats. 
 
 Steps: Open file -> Extract Data -> parse data -> Analyze data -> Send Report -> Close file 
In above steps: 
 Analyze and send report method will be same for each type of docs.
 
 
 ### Facade Pattern
 Eg: https://refactoring.guru/design-patterns/facade
 
 - Facade is a structural design pattern that provides a simplified (but limited) interface 
 to a complex system of classes, library or framework.
 
 
