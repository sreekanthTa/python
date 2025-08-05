# | Concept        | JavaScript Example | Python Example        |
# | -------------- | ------------------ | --------------------- |
# | Class          | `class Car {}`     | `class Car:`          |
# | Constructor    | `constructor()`    | `def __init__(self):` |
# | `this` keyword | `this.speed`       | `self.speed`          |
# | New instance   | `new Car()`        | `Car()`               |

javascript_example = """class Car {
    constructor(speed) {

        this.speed = speed;
    }
    accelerate() {
        console.log(`Accelerating at ${this.speed} km/h`);
    }
}
let myCar = new Car(100);
myCar.accelerate(); // Accelerating at 100 km/h
}"""

python_example = """class Car:
    def __init__(self, speed):
        self.speed = speed
    def accelerate(self):
        print(f"Accelerating at {self.speed} km/h")
my_car = Car(100)
my_car.accelerate()  # Accelerating at 100 km/h"""
print("JavaScript Example:\n", javascript_example)
print("\nPython Example:\n", python_example)


# ENCAPSULATION
# Encapsulation is the bundling of data and methods that operate on that data within a single unit, or class.
# It restricts direct access to some of an object's components, which can prevent the accidental modification
# of data. In Python, encapsulation is achieved through the use of private and public attributes.
class Person:
    def __init__(self, name, age_):
        self.name = name   # Public attribute
        self.__age = age_  # Private attribute, "__" prefix makes it private

    def get_age(self):
        return self.__age
    def set_age(self, age_):
        if age_ > 0:
            self.__age = age_
        else:
            print("Age must be positive")
person = Person("John", 30)
print("Name:", person.name)
print("Age:", person.get_age())  # Accessing private attribute through a method
person.set_age(35)  # Modifying private attribute through a method
print("Updated Age:", person.get_age())
# print("DirectAccess Age:", person.__age)  # This will raise an AttributeError since __age is private


# ABSTRACTION: Hiding complex implementation details and showing only the essential features of the object.
# In Python, abstraction can be achieved using abstract classes and interfaces.

# Just like you don’t need to know how print() works inside — you just use it.
# In OOP, abstraction often means:
# Designing methods that explain what the object does (not how).
# Keeping implementation details hidden (like helper methods or private logic).
# Using abstract classes or interfaces (for deeper abstraction, like in larger systems).

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
    def stop_engine(self):
        print("Bike engine stopped")

def main():
    my_car = Car()
    my_car.start_engine()  # Car engine started
    my_car.stop_engine()   # Car engine stopped

    my_bike = Bike()
    my_bike.start_engine()  # Bike engine started
    my_bike.stop_engine()   # Bike engine stopped

if __name__ == "__main__":
    main()




# Inheritance: Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
# This promotes code reuse and establishes a relationship between classes.
 
class Animal:
    def speak(self):
        return "Animal speaks"
    
    def eat(self):
        return "Animal eats"
    
class Dog(Animal):
    def speak(self):
          parent_message = super().speak()
          return parent_message + " & Dog barks"
        # return "Dog barks"
    
    def fetch(self):
        return "Dog fetches the ball"
    
 
    
def main():
    my_dog = Dog()
    print(my_dog.speak())  # Dog barks
    print(my_dog.eat())    # Animal eats
 
    # Using isinstance to check type
    print(isinstance(my_dog, Animal))  # True   


if __name__ == "__main__":
    main()



# POLYMORPHISM:
# Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.
# In Python, this is often achieved through method overriding and duck typing.


class Dog:
    def speak(self):
        return "Dog barks"

class Cat:
    def speak(self):
        return "Cat meows"
    
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Even though speak() is the same method name, it behaves differently for each animal — that is polymorphism.

class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())

# Output:
# Bark
# Meow

# In this example, both Dog and Cat classes override the make_sound method from the Animal class,
# demonstrating polymorphism. Each class provides its own implementation of the method, allowing for different behaviors    