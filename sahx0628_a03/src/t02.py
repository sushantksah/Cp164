"""
-------------------------------------------------------
[Assignment 3, Task 2]
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
stack1 = Stack()
stack2 = Stack()
target_stack = Stack()

# Inputs for Stack 1
stack1.push(1)
stack1.push(3)
stack1.push(5)

# Inputs for Stack 2
stack2.push(2)
stack2.push(4)
stack2.push(6)

# Target Stack
target_stack.push(10)
target_stack.push(20)
target_stack.push(30)

# Calling Function
target_stack.combine(stack1, stack2)

# Output
print(target_stack._values)
