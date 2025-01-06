"""
-------------------------------------------------------
[Assignment 2, Task 2]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import average_calories

# Sample list of Food objects
foods = [Food("Natto", 6, True, 212),
         Food("Pavlova", 10, True, 272),
         Food("Sushi", 6, True, 300),
         Food("Spanakopita", 5, False, 260), ]

avg_calories = average_calories(foods)

# Print the result
print(f"Average Calories: {avg_calories}")
