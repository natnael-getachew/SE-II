Mediator pattern is used in cases where many classes start
communicating amongst each other to produce result. When the software starts
getting developed, more user requests get added, this results in increased interaction with in the existing classes.
Which results a complex and difficult to maintain system.
In this pattern an object is defined that encapsulates how a set of objects interact.
Mediator promotes loose coupling by keeping objects(colleagues) from referring to
each other explicitly, and it lets you vary their interaction independently and all the colleagues interact through
the mediator.

I have implemented this pattern this pattern in a simple Taxi service example using the python programming language.
There is a ControlCenter class which is the Mediator class to coordinate between a customer and a taxi driver.
There is a Customer class which is a Colleague class which communicates with the control center whenever 
it would have otherwise communicated with a taxi driver.
There is a TaxiDriver class which is another Colleague class which communicates with the control center whenever 
it would have otherwise communicated with a customer.

   