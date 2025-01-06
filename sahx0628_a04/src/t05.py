"""
-------------------------------------------------------
[Assignment 4, Task 5]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

# Initalizing queue
pq = Priority_Queue()

# Adding values to queue
for value in [1, 3, 5, 7]:
    pq.insert(value)

# Defining Split Key
split_key = 4

# Split the priority queue based on the key
high, loweq = pq_split_key(pq, split_key)

# Target 1
print("Target 1 Queue:")
for value in high:
    print(value, end=' ')
print()

# Target 2
print("Target 2 Queue:")
for value in loweq:
    print(value, end=' ')
print()
