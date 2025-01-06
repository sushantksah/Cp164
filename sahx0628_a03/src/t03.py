"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
from Stack_array import Stack

# Calling Stack() Class
source = Stack()

# Input nums
source.push(1)
source.push(3)
source.push(5)

# BEfore
print(f"Stack before: {source._values}")

# Reversing Stack
stack_reverse(source)

# After
print(f"after: ")


while not source.is_empty():
    print(source.pop())
