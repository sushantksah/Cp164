"""
-------------------------------------------------------
[Assignment 3, Task 4]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Calling Stack()
source_stack = Stack()

#Putting in Values
source_stack._values.extend([1, 2, 3])

print(f"Before: {source_stack._values}")

# Reversing the Stack
source_stack.reverse()

print(f"After: {source_stack._values}")
