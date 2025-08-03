# 01.Parameter Order:

# def function(normal, *args, default_param=value, **kwargs):
# Let’s break that down:

# Type	What it means
# normal	Normal positional parameter
# *args	Collects extra positional arguments as a tuple
# default_param=val	Keyword param with default (can be overridden)
# **kwargs	Collects extra keyword arguments as a dict


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
greet("Sreekanth")  # Uses default greeting
greet("Sreekanth", "Hi")  # Overrides default greeting
# 02.Keyword Arguments:
# You can specify arguments by name, allowing you to skip some parameters
# or change their order.
greet(greeting="Hi", name="Sreekanth")  # Order doesn't matter with keyword arguments
# 03.Default Values:
# Default values can be set for parameters, allowing you to call the function
# without providing all arguments.
# If an argument is not provided, the default value is used.
greet("Sreekanth")  # Uses default greeting
# 04.Positional Arguments:
# Positional arguments are passed in the order they are defined in the function.
greet("Sreekanth", "Hi")  # Both arguments are positional
# 05.Mixing Positional and Keyword Arguments:
# You can mix positional and keyword arguments, but positional arguments must come first.
greet("Sreekanth", greeting="Hi")  # Positional first, then keyword


# 02. TUPLE UNPACKING:
t1 = (1, 2, 3)
t2 = (4, 5, 6)

a,b,c = t1  # Unpacking tuple into variables
print("Unpacked values:", a, b, c)

paris = [("Paris", "France"),
         ("Berlin", "Germany"),]
for city, country in paris:  # Unpacking tuple in loop
    print(f"{city} is in {country}")

# 03. DICTIONARY UPACKING:
d = {"name": "Sreekanth", "age": 30}
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")
display_info(**d)  # Unpacking dictionary into function arguments
