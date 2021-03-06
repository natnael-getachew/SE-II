In command pattern the object is encapsulated in the form of a command, i.e., 
the object contains all the information that is useful to invoke a method anytime user needs.
Command Pattern is associated with three components, the client, the invoker, and the receiver. Let‘s take a look at all the three components.
 Client: the Client represents the one that instantiates the encapsulated object.
 Invoker: the invoker is responsible for deciding when the method is to be invoked or called.
 Receiver: the receiver is that part of the code that contains the instructions to execute when a corresponding command is given.
The key to implementing this pattern is that the Invoker object should be kept away from specifics of what exactly happens when its methods are executed.
This way, the same Invoker object can be used to send commands to objects with similar interfaces.

I have implemented this pattern in a simple multiple-color light switching(ON or OFF) example using the python programming language:
There is a Switch class which is the Invoker class which asks to execute the TURNOFF or TURNON the lights. 
There are GreenLight, RedLight, and OrangeLight classes which are the Reciever classes which light up the lamps or undo it
(in this case, it just prints each light is on and each light is off). 
There is a LightSwitch class which is the client class which associates the FLIPUP AND FLIPDOWN commands to the reciever 