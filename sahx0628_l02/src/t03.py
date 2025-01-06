"""
-------------------------------------------------------
[Lab 2, Task 3]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
import utilities

# Initalizing Lists
stack = Stack()
target = []

# Calling Functions
utilities.array_to_stack(stack, [3, 6, 1, 5, 7])
utilities.stack_to_array(stack, target)

# Output
print(target)
