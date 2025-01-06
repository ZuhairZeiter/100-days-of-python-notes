# Day One of Python Learning

# Python Indentations
# Indentations are basically the spaces that we use while programming 
# in Python
# If you are wondering, which value is best for Indentations
# then the answer is 4 spaces!

# Let's print a statement
print("Hello, World!")

# Here, print is a python keyword, it is used to print something on the console.


# Introduction to Variables:
# Variables are containers for storing data values
# Think of it like a jar, containing your favorite cookies in it...

# Variables in Python:
# Variables are created when you assign a value to it.
# Variables are case sensitive
# Example:
x = 5
y = "John"
print(x)
print(y)
# Here, x and y are variables, and 5 and "John" are their assigned values.

# Python Indentifiers:
# An identifier is a name given to entities like class, functions, variables, etc.
# It helps to differentiate one entity from another.
# Rules for writing identifiers:
# 1. It should start with a letter (a-z, A-Z) or an underscore (_).
# 2. It can contain letters, digits, or underscores (_).
# 3. It should not start with a digit.
# 4. It should not be a reserved keyword in Python.
# Some examples of Identifiers are;
# my_variable = 5
# _my_variable = 10
# my_variable1 = 20
# my_variable_1 = 30
# my_variable_2 = 40

# Python Keywords:
# Keywords are the reserved words in Python.
# We cannot use a keyword as a variable name, function name, or any other identifier.
# They are used to define the syntax and structure of the Python language.
# Some examples of keywords are;
# if, else, elif, while, for, in, and, or, not, etc.
# Otherwise, the list will be provided after all, so no need to worry as well.
# You can check the list of keywords in Python by using the following code:
import keyword
print(keyword.kwlist)


# Python Comments:
# Comments are used to explain the code.
# Comments are ignored by the Python interpreter.
# Comments are used to make the code more readable.
# Comments are used to avoid confusion.
# Comments are used to avoid errors.
# Comments are used to avoid bugs.
# Comments are used to explain the code.

# There are two types of comments in Python:
# 1. Single Line Comment
# 2. Multi Line Comments

# Single Line Comment:
# Single line comments are written using the hash (#) symbol.
# Example:
# This is a single line comment.

# Multi Line Comments:
# Multi line comments are written using triple quotes (''' or """).
# Example:
'''
This is 
a multi
line comment
'''

# Multi Line Statements:
# Python allows you to write multiple statements in a single line using a semicolon (;).
# Example:
a = 5; b = 6; c = 7
print(a, b, c)

# Using Backslashes(\):
# You can use backslashes to split a statement into multiple lines.
# Example:
a = 5 + \
    6 + \
    7
print(a)

# Using Parentheses():
# You can use parentheses to split a statement into multiple lines.
# Example:

d = (5 +
    6 +
    7)
print(d)

# Python Operators:
# Operators are used to perform operations on variables and values.
# There are different types of operators in Python.
# Some examples of operators are:
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators
# We will discuss all these operators in detail in the upcoming days.

# Continuing a statement in python:
# Implicit Continuation:
# Python implicitly supports line continuation within parentheses (), square brackets [], and curly braces {}. 
# This is often used in defining multi-line lists, tuples, dictionaries, or function arguments.
# Example:
my_list = [1, 2, 3,
           4, 5, 6]
print(my_list)

# Explicit Continuation:
# You can explicitly continue a statement by using the backslash (\) character.
# Example:

my_string = "This is a \
multi-line string."
print(my_string)

# Python Data Types (FOR DAY 2 of Python)