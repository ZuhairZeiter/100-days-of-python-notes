# DAY Three OF LEARNING PYTHON

# 📌 Objective:
# Dive deeper into Python fundamentals of Loops in python

# 📖 Topic(s):
# 1. Introduction to Python Loops
# 2. Learning For Loops
# 3. Getting to know about While Loops
# 4. Mastering the Nested Loops

# 🧭  Table of Content(s):
# 1. While Loop in Python
# 2. For Loop in Python
# 3. Nested Loops in Python
# 4. Loop Control Statements
# 5. Internal Working of Loops

# 1. While Loop in Python
# The while loop in Python is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.

# Syntax:
# while condition:
    # statements

# Example:
# i = 1
# while i < 6:
    # print(i)
#     i += 1
# Output: 1 2 3 4 5

# 2. For Loop in Python
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
# Syntax:
# for item in sequence:
    # statements

# Example:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
# Output: apple banana cherry

# 3. Nested Loops in Python
# A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
# Syntax:
# for iterator_var in sequence:
    # statements (outer loop)
    # for iterator_var in sequence:
        # statements (inner loop)

# Example:
# for i in range(1, 6):
    # for j in range(1, 6):
        # print(i, j)
# Output: 1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5

# 4. Loop Control Statements
# There are different control statements in Python.
# Some examples of control statements are:
# 1. break
# 2. continue
# 3. pass
# 4. return
# We will discuss all these control statements in detail in the upcoming days.

# 5. Internal Working of Loops
# Before proceeding to this section, you should have a prior understanding of Python Iterators.

# Python Iterators:
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Example:
# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)
# print(next(my_iter))
# Output: 1

# Firstly, lets see how a simple for loops in Python looks like.
# Example: This Python code iterates through a list called fruits, containing “apple”, “orange” and “kiwi.” It prints each fruit name on a separate line, displaying them in the order they appear in the list.
# fruits = ["apple", "orange", "kiwi"]
# for fruit in fruits:
#     print(fruit)

# Here we can see the for loops that iterates over iterable object fruit which is a list. Lists, sets, dictionaries are few iterable objects while an integer object is not an iterable object. For loops can iterate over any of these iterable objects.

# This Python code manually iterates through a list of fruits using an iterator. It prints each fruit’s name one by one and stops when there are no more items in the list.
# Example:
# fruits = ["apple", "orange", "kiwi"]
# iter_obj = iter(fruits)
# while True:
#     try:
#         fruit = next(iter_obj)
#         print(fruit)
#     except StopIteration:
#         break

# Output:
# apple
# orange
# kiwi
# We can see that under the hood we are calling iter() and next() method. 

