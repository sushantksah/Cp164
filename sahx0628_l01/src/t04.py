"""
-------------------------------------------------------
[Lab 1, Task 4]
-------------------------------------------------------
Author:  Sushant Sah
ID:      169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_food

line = str(input(
    "Enter a vertical bar-delimited line of food data in the format name|origin|is_vegetarian|calories: "))

result4 = read_food(line)

print()
print(f"{result4}")
