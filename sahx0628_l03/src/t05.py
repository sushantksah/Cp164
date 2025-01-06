"""
-------------------------------------------------------
[Lab 3, Task 5]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue

q = Queue()
source = [1, 2, 3]
array_to_queue(q, source)

for v in q:
    print(v)
