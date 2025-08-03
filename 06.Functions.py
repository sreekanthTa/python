def testFunc():
    print("This is a test function.")
    return "Test completed successfully."

print(testFunc() )


# Named Arguments
def greet(name, age=30):
    print((f"Hello,  {name}!  You are {age} years old."))

greet("Alice")
greet("Bob", 25)


# Args
def add(*args):
    print("Arguments received:", args)
    return sum(args)
print("Sum of numbers:", add(1, 2, 3, 4, 5))

# Kwargs
def display_info(**kwargs):
    print("Keyword arguments received:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")


# Scopes
def outer_function():
    outer_var = "I am from the outer function"

    def inner_function():
        inner_var = "I am from the inner function"
        print(outer_var)  # Accessing outer variable
        print(inner_var)  # Accessing inner variable

    inner_function()
    # print(inner_var)  # This would raise an error, as inner_var is not accessible here
    print(outer_var)  # This is accessible here

outer_function()

# Global KeyWord: 
# Global variables can be accessed and modified inside functions using the global keyword
# but it's generally not recommended to use them unless necessary.

# What if we don’t use global?
# Then it just creates a new local variable with the same name.

global_var = "I am a global variable"
def global_function():
    global global_var
    global_var = "I have been modified globally"
    print(global_var)

global_function()
print("Global variable after modification:", global_var)



# Enclosing / Nonlocal Scope:
# Nonlocal variables are used in nested functions to refer to variables in the enclosing scope.
# For nested functions, you can use nonlocal to modify a variable in the enclosing (but not global) function:
 
def enclosing_function():
    enclosing_var = "I am from the enclosing function"

    def inner_function():
        nonlocal enclosing_var
        enclosing_var = "I have been modified in the inner function"
        print(enclosing_var)

    inner_function()
    print("Enclosing variable after modification:", enclosing_var)
enclosing_function()


# What is a docstring?
# A docstring is written as the first statement inside a function, and uses triple quotes (""" """ or ''' '''):
 

def greet(name):
    """This function greets the person passed in as an argument."""
    print(f"Hello, {name}!")

print(greet.__doc__)

# Why not just use comments?
# Comments (# like this) are ignored by Python. Docstrings are stored as part of the function's metadata — which means:

# You can get them dynamically (with help() or . __doc__)

# Tools like IDEs or documentation generators can display them