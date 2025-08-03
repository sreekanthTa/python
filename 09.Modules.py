# What is a Module?
# A module is just a .py file that contains Python code — functions, classes, or variables — that you can reuse in other files.

# You use modules to:

# Organize code

# Reuse logic

# Use built-in or third-party tools


# Types of Modules
# 1. Built-in modules → come with Python
#    Examples: math, random, sys, os

# import math
# print(math.sqrt(16))  # 4.0

# Or 

# import just what you need:

# from math import sqrt
# print(sqrt(25))  # 5.0



# 2. Custom modules → your own .py files

# utils.py
# def greet(name):
#     return f"Hello, {name}!"

# from utils import greet
# print(greet("Sree"))  # Hello, Sree!


# 3. Third-party modules → installed via pip
#    Examples: requests, numpy, pandas

# pip install requests
# Then in your Python file:
 
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)


# 4. Standard Library → comes with Python, no need to install
#    Examples: datetime, json, re
# MAIN: It runs when the file is executed directly, but not when imported as a module.
# if __name__ == "__main__":
#     print("This runs only when the file is run directly")
# This is useful for testing or running code that should only execute when the file is run directly, not when imported.
# Example of a module with main
def main():
    print("This is the main function of the module.")   
    

if __name__ == "__main__":
    print("This runs only when the file is run directly")
