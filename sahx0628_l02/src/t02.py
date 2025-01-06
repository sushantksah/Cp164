"""
-------------------------------------------------------
[Lab 2, Task 2]
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

# Initalizing Function
stack = Stack()
source = [2, 6, 4, 2, 5]

# Calling Function
utilities.array_to_stack(stack, source)

# Output
while stack.is_empty() == False:
    print(stack.pop())
