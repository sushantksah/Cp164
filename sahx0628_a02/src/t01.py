"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import by_origin

# Sample list to test
foods = [Food("Natto", 6, True, 212),
         Food("Pavlova", 10, True, 272),
         Food("Sushi", 6, True, 300),
         Food("Spanakopita", 5, False, 260), ]

# Origin Point
origin = 6

# Calling Function
origins = by_origin(foods, origin)

# Ouput
for f in origins:
    print(f.name)
