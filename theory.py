1 Question: Define Obejct Oriented Programming Language?
Ans:An “Object” is the key component of Object-oriented programming. An Object may contain data (fields or variables) or code (methods or procedures). The creation of these objects is based on a programmer-defined blue-print also known as a Class.

2 Question: Lists down benefits of OOP?
Ans:(1)It provides a clear modular structure for programs which makes it good for defining abstract datatypes in which implementation details are hidden.
(2)Objects can also be reused within an across applications. The reuse of software also lowers the cost of development. More effort is put into the object-oriented analysis and design, which lowers the overall cost of development.
(3)It makes software easier to maintain. Since the design is modular, part of the system can be updated in case of issues without a need to make large-scale changes.
(4)Reuse also enables faster development. Object-oriented programming languages come with rich libraries of objects, and code developed during projects is also reusable in future projects.
(5)It provides a good framework for code libraries where the supplied software components can be easily adapted and modified by the programmer. This is particularly useful for developing graphical user interfaces.

3 Question:Differentiate between function and method?
Ans:A function has another property: all calls to a function with the same parameters, should return the same result. A method, on the other hand, is a function that is related to an object in an object-oriented language. It has one implicit parameter: the object being acted upon.

4 Question:Define the following term?
Ans: (1)Class:- In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.
(2)Object:-n object-oriented programming (OOP), objects are the things you think about first in designing a program and they are also the units of code that are eventually derived from the process.
(3)Attributes:-Attributes are data stored inside a class or instance and represent the state or quality of the class or instance.
(4)Behaviour:-Behavior is the only way objects can do anything to themselves or have anything done to them.

Question 5:
Ans:
CODING:-

#class
##instantiation method
def _init_(car,name,model,colour,year,hp):
    ##attributes and attributes names
    Car.name=name
    Car.model=model
    Car.colour=colour
    Car.year=year
    Car.hp=hp
    ##default attribute
    Car.compname='Honda'
    
    def update company name(Car,NewName):
        Car.compname=NewName
        ##instance
        Car1=car('GTS','Honda Civic','silver',2020,2019)
        print(Car1.name)
        print(Car1.model)
        print(Car1.year)
        print(Car1.hp)
        print(Car1.compname)
        Car1.updatecomp name(HondaMotorCo)
        print(Car1.complete,'Modified Name')
        print('\n')
        
        ##new instance of Car 2 
        Car2= Car('Petrol','Safari','Black',2019,200)
        print(Car2.name)
        print(Car2.model)
        print(Car2.year)
        print(Car2.hp)
        print('\n')
        print(Car1)
        print(Car2)

