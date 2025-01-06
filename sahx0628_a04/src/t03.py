"""
-------------------------------------------------------
[Assignment 4, Task 3]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
from functions import queue_split_alt

# Intializing Queues
source = Queue()
temp = Queue()

# Adding Values to Queue
for i in range(8):
    source.insert(i)
    temp.insert(i)

# Prints out all the values of Source
print(f"source contains: ")
while not temp.is_empty():
    print(temp.remove(), end=' ')

# Calling Function
target1, target2 = queue_split_alt(source)

# Space
print()

# Prints even numbers in Source
print("target1 contains:")
while not target1.is_empty():
    print(target1.remove(), end=' ')

# Space
print()

# Prints Odd Numbers in Source
print("target2 contains:")
while not target2.is_empty():
    print(target2.remove(), end=' ')
