"""
-------------------------------------------------------
[Assignment 4, Task 6]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

# Initalizing Variable
pq = Priority_Queue()

# Adding values to Queue
for value in [100, 48, 18, 75, 60, 150]:
    pq.insert(value)

# Initalizing Key
key = 50

# Calling Function
loweq, high = pq.split_key(key)

# Shows Original Priority Queue
print("Original Priority Queue:")
if not pq.is_empty:
    print()

# Space
print()

# Shows all values in the queue that are higher than the key
print("Queue with values > than key:")
for value in high:
    print(value, end=' ')
print()

# Space
print()

# Shows all values in the queue that are lower than or equal to the key
print("Queue with values < than or = to key:")
for value in loweq:
    print(value, end=' ')
print()
