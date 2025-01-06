"""
-------------------------------------------------------
[Lab 5, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List

shopping = List()
shopping.prepend("Apples")
shopping.append("Bananas")
shopping.insert(0, "Samsung Smart Fridge")

for item in shopping:
    print(item)
