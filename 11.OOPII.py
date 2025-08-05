
# Dunder methods in Python
# Dunder methods (double underscore methods) are special methods that start and end with double underscores
# They allow you to define the behavior of your objects for built-in operations like addition, string representation, etc.
# Common dunder methods include:
# __init__() for object initialization
# __str__() for string representation and printing
# __repr__() for unambiguous string representation
# __add__() for addition
# __len__() for length
# Example of a class with dunder methods    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # your __str__ method here, Meant for readable (user-friendly) output.
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    # your __repr__ method here, Meant for unambiguous (developer-friendly) output.
    def __repr__(self):
        return f"Repr: Person(name='{self.name}', age={self.age})"
    
    # your __len__ method here
    def __len__(self):
        return self.age  # Assuming age represents the number of pages in a book
    
    # your __add__ method here
    def __add__(self, other):
        return Person(self.name + " & " + other.name, self.age + other.age)

person = Person("Alice", 30)
print(str(person)) # Using __str__
print(repr(person)) # Using __repr__
print(len(person))  # Using __len__
person2 = Person("Bob", 25)
combined_person = person + person2  # Using __add__
print(combined_person)  # Using __str__ of combined person

# Try removing __str__() and only keeping __repr__(). Now print(book) will fall back to __repr__().




