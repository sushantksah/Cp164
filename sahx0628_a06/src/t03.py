"""
-------------------------------------------------------
[Assignment 5, Task 2]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
from Deque_linked import Deque

# Initalizing Queue
deque = Deque()

# Original Queue / Inserting Values at the rear
for value in [1, 9, 99, 11, 19]:
    deque.insert_rear(value)
print("Deque after inserting values at rear:")
for value in deque:
    print(value, end=' ')
print()

print()

# Instering Values at the front
for value in [0, -14, -23, 0, -11]:
    deque.insert_front(value)
print("Deque after inserting values at front:")
for value in deque:
    print(value, end=' ')
print()

print()

# Removing Values
front_value = deque.remove_front()
rear_value = deque.remove_rear()
# Showing what was removed
print(f"Removed from front: {front_value} and Removed from rear: {rear_value}")

print()

# Showing Front/Back Value
front_peek = deque.peek_front()
rear_peek = deque.peek_rear()
print(f"Peek front: {front_peek}, Peek rear: {rear_peek}")
print()

# is empty ????
print("Is empty????", deque.is_empty())

print()

# Length ???
print("Length:", len(deque))

# Instering Rear
deque2 = Deque()
for value in [-2, -1, 0, 1, 2, 3, 4]:
    deque2.insert_rear(value)
print()

# RQUALITY???
print("Are equal???", deque == deque2)
print()

# Iteratorr
print("Iterating through the deque:")
for value in deque:
    print(value, end=' ')
print()
