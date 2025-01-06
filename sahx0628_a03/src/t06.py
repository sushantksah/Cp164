"""
-------------------------------------------------------
[Assignment 3, Task 6]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import postfix

# Test Tuple
test = [
    "12 5 -",
    "4 5 + 12 * 2 3 * -",
    "7 2 + 3 /"
]

result_1 = postfix(test[0])
print(f"'{test[0]}' = {result_1}")

result_2 = postfix(test[1])
print(f"'{test[1]}' = {result_2}")

result_3 = postfix(test[2])
print(f"'{test[2]}'= {result_3}")
