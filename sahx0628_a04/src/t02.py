"""
-------------------------------------------------------
[Assignment 4, Task 2]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

# Initalizing Queues
queue1 = Queue()
queue2 = Queue()

# Adding values to the Queue
for element in [1, 2, 3, 4, 5]:
    queue1.insert(element)
    queue2.insert(element)

# Checking equality
if queue1.__eq__(queue2):
    print("Queue1 and queue2 are equal.")
else:
    print("Queue1 and queue2 are not equal.")

# Change the Queue
queue2.remove()
queue2.insert(70)

print()

# Checking if queues are still equal
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("Now, queue1 and queue2 are not equal.")
