"""
-------------------------------------------------------
[Lab 3, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports

from Queue_array import Queue

q = Queue()

newnum = [9]

print("Adding Element to Queue:")

for i in newnum:
    q.insert(newnum)
    print(f"Queue: {[val for val in q]}")
