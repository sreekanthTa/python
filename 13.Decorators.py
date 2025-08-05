# What is a Decorator ?
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
# Decorators are often used to add functionality to existing functions or methods, such as logging,
# access control, or caching.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Example usage of a decorator
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# In this example, `my_decorator` is a decorator that wraps the `say_hello` function.
# When `say_hello` is called, it first executes the code in the `wrapper
#` function, which adds behavior before and after the original function call.
# Decorators can also take arguments, allowing for more flexible behavior.
