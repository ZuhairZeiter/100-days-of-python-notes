# DAY Five OF LEARNING PYTHON

# 📌 Objective:
# Dive deeper into Python fundamentals of Functions in python (Part II of III)

# 📖 Topic(s):
# 1. Introduction to Python Function Arguments
# 2. Types of Functions Arguments in Python
# 3. Detailed study of; Default, Keyword, Positional & Arbitrary
# 4. Deep Dive to Docstring

# 🧭  Table of Content(s):
# 1. Getting to know Function Arguments
# 2. Learning the types of Function Arguments
# 3. Detailed study of Function Arguments Types
# 4. A deep dive to Docstring
# 5. Upcoming Topic Discussion


# Introduction to Python Function Arguments
# Function arguments are the values that are passed to a function when it is called.
# Function arguments can be of different types, such as integers, strings, or even other functions.
# When a function is called, the arguments are passed to the function as parameters.
# Example:
def add_numbers(a, b):
    return a + b

# Learning the types of Function Arguments
# There are four types of function arguments in Python:
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Positional Arguments
# 4. Arbitrary Arguments

# Detailed study of Function Arguments Types
# 1. Default Arguments
# Default arguments are arguments that have a default value assigned to them.
# If the function is called without an argument for a default argument, the default value is used.
# Example:

def greet(name="User"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, User!

# 2. Keyword Arguments
# Keyword arguments are arguments that are passed to a function using their names.
# Keyword arguments are useful when you want to pass arguments in a specific order.
# Example:

def multiply(x, y):
    return x * y

print(multiply(y=5, x=3))  # Output: 15

# 3. Positional Arguments
# Positional arguments are arguments that are passed to a function in the order they are specified.
# Positional arguments are useful when you want to pass arguments in a specific order.
# Example:

def divide(a, b):
    return a / b

print(divide(10, 2))  # Output: 5.0

# 4. Arbitrary Arguments
# Arbitrary arguments are arguments that are passed to a function as a tuple.
# Arbitrary arguments are useful when you want to pass a variable number of arguments to a function.
# Example:

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5))  # Output: 15 

# A deep dive to Docstring
# Docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
# It is used to document the module, function, class, or method.
# Docstrings are important for documentation purposes and are used to communicate the purpose of the module, function, class, or method.
# Example:

def add_numbers(a, b):
    """
    This function adds two numbers.
    :param a: The first number.
    :param b: The second number.
    :return: The sum of the two numbers.
    """
    return a + b

# Upcoming Topic Discussion:
# We will discuss about the following topics in the upcoming days:
# 1. Python Function within Functions
# 2. Anonymous Functions in Python
# 3. Recursive Functions in Python
# 4. Return Statement in Python Function
# 5. Pass by Reference and Pass by Value