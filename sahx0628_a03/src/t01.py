"""
-------------------------------------------------------
[Assignment 3, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_combine

# Calling Stack
stack1 = Stack()
stack2 = Stack()

# Inputs for Stack 1
stack1.push(1)
stack1.push(3)
stack1.push(9)
# Inputs for Stack 2
stack2.push(2)
stack2.push(4)
stack2.push(6)

# Calling Function
comb_stack = stack_combine(stack1, stack2)

# Output
for item in comb_stack:
    print(item)
