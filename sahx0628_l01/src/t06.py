"""
-------------------------------------------------------
[Lab 1, Task 6]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import write_foods

file_variable = open("new_foods.txt", "r+")
foods = []

new_food = str(input("Enter a new food object {foramt: name|origin|is_vegetarian|calories}: "))

while new_food != "":
    foods.append(new_food)
    new_food = input("Enter a new food object {format: name\origin\is_vegetarian|calories}: ")

write_foods(file_variable, foods)

file_variable.close()
