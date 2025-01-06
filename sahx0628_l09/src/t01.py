"""
-------------------------------------------------------
[Lab 9, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Food import Food

food1 = Food("Teppanyaki", 6, False, 200)
food2 = Food("Greek Salad", 5, True, 185)
food3 = Food("Fettacuccine", 7, False, 266)

foods = []
foods.append(food1)
foods.append(food2)
foods.append(food3)

hash_table(7, foods)
