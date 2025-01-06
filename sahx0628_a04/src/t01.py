"""
-------------------------------------------------------
[Assignment 4, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

# Intializing Queue
queue = Queue()

# Testing Insert
print("Insert Test")
for k in range(2):
    queue.insert(k)
    print(f"{k} was inserted into the Queue.")

print()

# Testing if a queue is full
if queue.is_full():
    print("The queue is full.")
else:
    print("The queue is not full.")

print()

# Testing if the queue is empty
if queue.is_empty():
    print("The queue is empty.")
else:
    print("The queue is not empty.")

print()

# Showing the first element in the queue
first_element = queue.peek()
print(f"The first element in the queue is: {first_element}")

print()

# Testing Remove
removed_element = queue.remove()
print(f"Removed element: {removed_element}")

print()

# Shows how many things are in the queue
print(f"The queue has {len(queue)} elements.")

print()

# Initializing Queue2
Queue2 = Queue()
for i in range(5):
    Queue2.insert(i)

# Testing if Queues are Equal
if queue == Queue2:
    print("NOT EQUAL.")
else:
    print("EQUAL.")

print()

# Showing all the alues in Queue
print("Iterating over the queue:")
for value in queue:
    print(value)
