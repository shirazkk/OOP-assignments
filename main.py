
"""

1. Using self
Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

"""

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

    
#     def display(self):
#         print(f"{self.name} secure {self.marks} marks in 12th grade")


# student1 = Student("shiraz",60)

# student1.display()


"""

2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

"""

# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count +=1
        

#     @classmethod
#     def track(cls):
#         print(cls.count)


# obj1 = Counter() 
# Counter.track()   
# obj2 = Counter()  
# Counter.track()   
# obj3 = Counter()  
# Counter.track()   
# obj4 = Counter()  
# Counter.track()   



"""

3. Public Variables and Methods
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

"""

# class Car:
#     def __init__(self,brand):
#         self.brand = brand

#     def start(self):
#         print(f"{self.brand} is a car")

# obj = Car("Camere")
# print(obj.brand)
# obj.start()


"""

4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

"""

# class Bank:
#     bank_name = "HBL"

#     @classmethod
#     def change_bank_name(cls,name):
#         cls.bank_name = name
#         print(f"Bank name is now {name}")


# obj1 = Bank()
# obj1.change_bank_name("UBL")
# print(obj1.bank_name)

# obj2 = Bank()
# obj2.change_bank_name("islami Bank")
# print(obj2.bank_name)



"""

5. Static Variables and Static Methods
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

"""

# class MathUtlish:

#     @staticmethod
#     def add(a,b):
#         return a+b
    

# obj1 = MathUtlish()
# print(obj1.add(1,2))


"""

6. Constructors and Destructors
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

"""

# class Logger:
#     def __init__(self):
#         print("object is created!")


#     def __del__(self):
#         print("object is destroyed")


# obj = Logger()

# del obj


"""

7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.

"""


# class Employee:
#     def __init__(self,name,salary,ssn) -> None:
#         self.name = name
#         self._salary = salary
#         self.__ssn = ssn
        
#     def employee1(self):
#         print(f"{self.name}, {self._salary}, {self.__ssn}")

# obj=Employee("jack",2000,33)

# print(obj.name)
# print(obj._salary)
# # print(obj.__ssn) #error python use name mangling to restrict direct access of private attribute
    


"""

8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

"""

# class Person:
#     def __init__(self,name):
#         self.name = name


# class Teacher(Person):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject = subject

# # Example Usage
# teacher = Teacher("Alice", "Math")
# print(teacher.name)  # Output: Alice
# print(teacher.subject)  # Output: Math


"""

9. Abstract Classes and Methods
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

"""

# from abc import ABC , abstractmethod

# class Shape(ABC):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
    
#     def area(self):
#         print(f"Area = {self.length * self.width}")


# rec = Rectangle(2,4)
# rec.area()



"""

10. Instance Methods
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

"""

# class Dog:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} is the breed of  {self.breed}")


# obj = Dog("jack","german shepard")
# obj.bark()


"""

11. Class Methods
Assignment:
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


"""

# class Book:
#     total_books=0

#     @classmethod
#     def increment_book_count(cls,new_book):
#         cls.total_books +=1
#         print(f"new book is added:{new_book}")


# print(Book().total_books)
# Book().increment_book_count("love")
# print(Book().total_books)
# Book().increment_book_count("Fight")
# print(Book().total_books)



"""

12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

"""

# class TemperatureConverter:

#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return f"Fahrenheit Value is: {c}"


# obj = TemperatureConverter()
# print(obj.celsius_to_fahrenheit(100))


"""

13. Composition
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

"""

# class Engine:

#     def start(self):
#         print("Engine is started!")

# class Car:
#     def __init__(self) -> None:
#         self.engine = Engine()

#     def drive(self):
#         self.engine.start()
#         print("Car is moving")


# obj = Car()
# obj.drive()


"""

14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

"""

# class Department:
#     def __init__(self,name):
#         self.name = name


# class Employee:
#     def __init__(self,name,department):
#         self.name = name
#         self.department = department

#     def work(self):
#         print(f"{self.name} is Working in {self.department.name} department!")


# department1 = Department("HR")


# employee1 = Employee("jack", department1)

# employee1.work()
        

# del department1

# employee1.work()



"""

15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.


"""

# class A:

#     def show(self):
#         print("i am call from class A")

# class B(A):

#     def show(self):
#         print("I am call from class B")

# class C(A):
    
#     def show(self):
#         print("I am call from class C")

# class D(B,C):
#     pass


# obj = D()

# obj.show()

# print(D.__mro__)


"""

16. Function Decorators
Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

"""

# def log_function_call(func):
#     def wrapper():
#         print("Function is being called")
#         func()
#     return wrapper

# @log_function_call
# def say_hello():
#     print("Hello!")

# say_hello()
