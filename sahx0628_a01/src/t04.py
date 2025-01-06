"""
-------------------------------------------------------
[Assignment 1, Task 4]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

# Opening file
f = "test.txt"
fv = open(f, "r", encoding="utf-8")

# Calling Functions
upp, low, dig, whi, rem = file_analyze(fv)
print("uppers: ", upp)
print("lowers: ", low)
print("digits: ", dig)
print("whitespace: ", whi)
print("other: ", rem)

# Checking for y
w = "try"
if w.__contains__("y"):
    print("Not in it")
