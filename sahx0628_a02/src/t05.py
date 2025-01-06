"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_search
from Food import Food

count = 0

# Sample List
food = Food("Apple", 3, True, 5)
food1 = Food("Beef", 2, False, 67)
food2 = Food("Water", 3, True, 10)
food3 = Food("Fish", 3, True, 0)
foods = [food, food1, food2, food3]
result = food_search(foods, -1, 0, True)

# Output
for f in result:
    print(f)
    print()
