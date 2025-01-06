"""
-------------------------------------------------------
[Lab 1, Task 5]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods

file_variable = open("foods.txt", "r")

result5 = read_foods(file_variable)

file_variable.close()
