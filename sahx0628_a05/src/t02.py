"""
-------------------------------------------------------
[Assignment 5, Task 2]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List
from Food_utilities import read_foods
from copy import deepcopy
from Food import Food

# Opening File
fh = open("foods.txt", "r", encoding="utf-8")

# Adding Values to test to a list from foods file
foods = read_foods(fh)
food_list = Sorted_List()
for food in foods:
    food_list.insert(food)


print("Testing Get Item: ")
if len(food_list) > 0:
    print(f"Get item:", food_list[0])

print()

print("Testing Clean: ")
food_list.clean()
print("List: ", [str(food) for food in food_list])

print()

print("Testing Combine: ")
list1 = Sorted_List()
list1.insert(foods[0])
list2 = Sorted_List()
list2.insert(foods[1])
food_list.combine(list1, list2)
print("List:", [str(food) for food in food_list])

print()

print("Testing Intersection: ")
list1 = deepcopy(food_list)
list2 = deepcopy(food_list)
list1.intersection(list1, list2)
print("List:", [str(food) for food in food_list])

print()

print("Testing Remove_Front: ")
if not food_list.is_empty():
    food_list.remove_front()
print("List:", [str(food) for food in food_list])

print()

print("Testing Remove_Many: ")
if len(food_list) > 0:
    food_list.remove_many(food_list[0])
print("List:", [str(food) for food in food_list])

print()

print("Testing Split")
if len(food_list) > 0:
    list1, list2 = food_list.split()
    print("List 1:", [str(food) for food in list1])
    print("List 2:", [str(food) for food in list2])

print()

print("Testing Split_ALT")
if len(food_list) > 0:
    list1, list2 = food_list.split_alt()
    print("List 1:", [str(food) for food in list1])
    print("List 2: ", [str(food) for food in list2])

print()

print("Testing Union")
list1 = Sorted_List()
list2 = Sorted_List()
list1.insert(foods[0])
list2.insert(foods[1])
food_list.union(list1, list2)
print("List:", [str(food) for food in food_list])

print()

print("Testing Equality: ")
list1 = Sorted_List()
list1.insert(foods[0])
list2 = Sorted_List()
list2.insert(foods[0])
print("Equality?:", list1 == list2)

print()

# Test __iter__
for food in food_list:
    print(food)
