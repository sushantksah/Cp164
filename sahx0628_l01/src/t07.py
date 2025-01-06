"""
-------------------------------------------------------
[Lab 1, Task 7]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import get_vegetarian, read_foods

file_variable = open("foods.txt")

foods = read_foods(file_variable)

result7 = get_vegetarian(foods)

for result in result7:
    print()
    print(f"{result}")
