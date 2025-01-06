"""
-------------------------------------------------------
[Assignment 4, Task 4]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

# Initalizing Queue
source_queue = Queue()

# Adding Values to Queue
for i in range(20):
    source_queue.insert(i)

# Splitting the Queue
target1, target2 = source_queue.split_alt()

# Even Queue
print("Target 1 Queue:")
for value in target1:
    print(value, end=' ')
print()

# Space
print()

# Odd Queue
print("Target 2 Queue:")
for value in target2:
    print(value, end=' ')
print()
