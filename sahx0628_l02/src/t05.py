"""
-------------------------------------------------------
[Lab 2, Task 5]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Food_utilities import read_foods
import utilities

fh = open("foods.txt", "r", encoding="utf-8")

source = read_foods(fh)

utilities.stack_test(source)
