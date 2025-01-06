"""
-------------------------------------------------------
[Assignment 5, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

# Defining Queues
queue1 = Queue()
queue2 = Queue()
queue3 = Queue()

# Instering values into the Queue
for i in range(1, 7):
    queue1.insert(i)

# 2nd Queue
for i in range(1, 9):
    queue2.insert(i)

# Checking is_empty
print(f"is empty? {queue1.is_empty()}")
print(f"is empty? {queue2.is_empty()}")
print()

# Peeking at the Front
print(f"Peeking at Queue1: {queue1.peek()}")
print(f"Front value of Queue2: {queue2.peek()}")
print()

# Removing from Queues
print(f"Removed out of Queue1: {queue1.remove()}")
print(f"Removed out of Queue2: {queue2.remove()}")
print()

# Combining the Queues
queue3.combine(queue1, queue2)
print("Queue3 after combining Queue1 and Queue2:")
for value in queue3:
    print(value, end=" ")
print()

print()
# Splitting the Queue
queue1, queue2 = queue3.split_alt()
print("Queue1 after splitting Queue3:")
for value in queue1:
    print(value, end=" ")
print()

print("Queue2 after splitting Queue3:")
for value in queue2:
    print(value, end=" ")
print()

print()

# Lengths of the Queues
print(f"Length of Queue1: {len(queue1)}")
print(f"Length of Queue2: {len(queue2)}")

# Checking append
queue1._append_queue(queue2)
print("Queue1 after appending Queue2:")
for value in queue1:
    print(value, end=" ")
print()

# EQ TESTINGGGGGG
nq = Queue()
nq.insert(1)
print()
print(f"Is Queue1 equal to new_queue? {queue1 == nq}")
print()
nq._append_queue(queue1)
print(f"Is Queue1 equal to new_queue after appending? {queue1 == nq}")
