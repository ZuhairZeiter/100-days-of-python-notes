# Day Two of Python Learning

# 📌 Objective:
# Dive deeper into Python fundamentals and explore control flow concepts.

# 📖 Topic(s):
# 1. Data Types and Type Conversion
# 2. Input/Output In Python
# 3. Python Operators (Arithmetic, Comparison, Logical, etc.)
# 4. Conditional Statements (if, else, elif) and their structure

# Python Data Types:
# Data types are the categories that group values together.
# There are different types of data types in Python.
# Some examples of data types are:
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean    
# 5. List
# 6. Tuple
# 7. Dictionary
# 8. Set
# 9. None
# We will discuss all these data types in detail in the upcoming days.  

# Python Strings:
# Strings are used to store text data in Python.
# Strings are immutable.
# Strings are enclosed in single quotes (' ') or double quotes (" ").
# Example:
name = 'John'
print(name)

# Python Integer:
# Integers are used to store whole numbers in Python.
# Integers are immutable.
# Example:
age = 25
print(age)

# Python Float:
# Floats are used to store decimal numbers in Python.
# Floats are immutable.
# Example:
height = 5.5
print(height)

# Python Boolean:
# Booleans are used to store True or False values in Python.
# Booleans are immutable.
# Example:
is_student = True
print(is_student)

# Python List:
# Lists are used to store multiple items in a single variable.
# Lists are mutable.
# Lists are enclosed in square brackets ([]).
# Example:
students = ['John', 'Alice', 'Bob']
print(students)

# Python Tuple:
# Tuples are used to store multiple items in a single variable.
# Tuples are immutable.
# Tuples are enclosed in parentheses ().
# Example:
coordinates = (10, 20)
print(coordinates)

# Python Dictionary:
# Dictionaries are used to store key-value pairs in Python.
# Dictionaries are mutable.
# Dictionaries are enclosed in curly braces ({}).
# Example:
person = {'name': 'John', 'age': 25}
print(person)

# Python Set:
# Sets are used to store unique items in Python.
# Sets are mutable.
# Sets are enclosed in curly braces ({}).
# Example:
fruits = {'apple', 'banana', 'orange'}
print(fruits)

# Python None:
# None is used to represent the absence of a value.
# None is a data type.
# None is immutable.
# Example:
value = None

# Type of a variable:
# You can check the type of a variable using the type() function.
# Example:
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(students))
print(type(coordinates))
print(type(person))
print(type(fruits))
print(type(value))

# Input and Output In Python:
# You can take input from the user using the input() function.
# You can display output to the user using the print() function.
# Example:
name = input('Enter your name: ')
print('Hello, ' + name + '!')

# String Formatting:
# You can format strings using the format() method.
# Example:
name = 'John'
age = 25
print('My name is {} and I am {} years old.'.format(name, age))

# String Slicing:
# You can slice strings using the slice() function.
# Example:
name = 'John'
print(name[0:2])

# String Methods:
# There are many string methods in Python.
# Some examples of string methods are:
# 1. capitalize()
# 2. casefold()
# 3. center()
# 4. count()
# 5. encode()
# 6. endswith()
# 7. expandtabs()
# 8. find()
# 9. format()
# 10. format_map()
# 11. index()
# 12. isalnum()
# 13. isalpha()
# 14. isdecimal()
# 15. isdigit()
# 16. isidentifier()
# 17. islower()
# 18. isnumeric()
# 19. isprintable()
# 20. isspace()
# 21. istitle()
# 22. isupper()
# 23. join()
# 24. ljust()
# 25. lower()
# 26. lstrip()
# 27. maketrans()
# 28. partition()
# 29. replace()
# 30. rfind()
# 31. rindex()
# 32. rjust()
# 33. rpartition()
# 34. rstrip()
# 35. split()
# 36. splitlines()
# 37. startswith()
# 38. strip()
# 39. swapcase()
# 40. title()
# 41. translate()
# 42. upper()
# 43. zfill()
# We will discuss all these string methods in detail in the upcoming days.


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


# Conditional Statements:
# Conditional statements are used to execute a block of code if a certain condition is true.
# There are different types of conditional statements in Python.
# Some examples of conditional statements are:
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. nested if statement
# We will discuss all these conditional statements in detail in the upcoming days.
# Loops:
# Loops are used to repeat a block of code multiple times.
# There are different types of loops in Python.
# Some examples of loops are:
# 1. for loop
# 2. while loop
# We will discuss all these loops in detail in the upcoming days.

# Structure of Conditional Statements:
# The structure of a conditional statement is as follows:
# if condition:
    # code block

# Example:
x = 10

if x > 5:
    print('x is greater than 5')

# Structure of if-else Statement:
# The structure of an if-else statement is as follows:
# if condition:
    # code block
# else:
    # code block

# Example:
x = 10

if x > 5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')

# Structure of if-elif-else Statement:
# The structure of an if-elif-else statement is as follows:
# if condition:
    # code block
# elif condition:
    # code block
# else:
    # code block

# Example:
x = 10

if x > 5:
    print('x is greater than 5')
elif x < 5:
    print('x is less than 5')
else:
    print('x is equal to 5')

# Structure of Nested if Statement:
# The structure of a nested if statement is as follows:
# if condition:
    # code block
    # if condition:
        # code block
    # else:
        # code block
# else:
    # code block    

# Example:
x = 10

if x > 5:
    print('x is greater than 5')
    if x < 10:
        print('x is less than 10')
    else:
        print('x is not less than 10')
else:
    print('x is not greater than 5')
