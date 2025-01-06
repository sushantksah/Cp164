"""
-------------------------------------------------------
[Assignment 5, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from Food import Food
from Food_utilities import read_foods
from List_array import List

# Opening File
fh = open("foods.txt", "r", encoding="utf-8")

# Adding Values to test to a list from foods file
foods = read_foods(fh)
food_list = List()
for food in foods:
    food_list.append(food)


print("Tesing __getitem__: ")
if len(food_list) > 0:
    print("Get item:", food_list[0])

print()

print("Testing Clean Function: ")
food_list.clean()
print("List after clean:", [str(food) for food in food_list])

print()

print("Testing Combine Functions: ")
list1 = List()
list1.append(foods[0])
list2 = List()
list2.append(foods[1])
food_list.combine(list1, list2)
print("List after combine:", [str(food) for food in food_list])

print("Testing Intersection Function: ")
list1 = deepcopy(food_list)
list2 = deepcopy(food_list)
list1.intersection(list1, list2)
print("List after intersection:", [str(food) for food in food_list])

print()

print("Testing Prepend Function: ")
food_list.prepend(Food("Test Food", 0, True, 100))
print("List after prepend:", [str(food) for food in food_list])

print()

print("Testing Remove_Front Function: ")
if not food_list.is_empty():
    food_list.remove_front()
print("List after remove_front:", [str(food) for food in food_list])

print()

print("Testing Remove_Many Function: ")
if len(food_list) > 0:
    food_list.remove_many(food_list[0])
print("List after remove_many:", [str(food) for food in food_list])

print()

print("Testing Split: ")
if len(food_list) > 0:
    list1, list2 = food_list.split()
    print("List 1 after split:", [str(food) for food in list1])
    print("List 2 after split:", [str(food) for food in list2])

print()

print("Testing Split Alt: ")
if len(food_list) > 0:
    list1, list2 = food_list.split_alt()
    print("List 1 after split_alt:", [str(food) for food in list1])
    print("List 2 after split_alt:", [str(food) for food in list2])

print()

print("Testing Union: ")
list1 = List()
list2 = List()
list1.append(foods[0])
list2.append(foods[1])
food_list.union(list1, list2)
print("List after union:", [str(food) for food in food_list])

print()

print("Testing Equality of Lists: ")
list1 = List()
list1.append(foods[0])
list2 = List()
list2.append(foods[0])
print("List1 equal List2:", list1 == list2)

print()

# Test __iter__
for food in food_list:
    print(food)
