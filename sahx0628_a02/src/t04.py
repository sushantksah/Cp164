"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import food_table

# Sample List
all_foods = [
    Food("Canada Goose Chili", 0, False, 199),
    Food("Spanakopita", 5, True, 260), ]

all_foods.sort()

# Output
food_table(all_foods)
