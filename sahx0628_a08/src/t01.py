"""
-------------------------------------------------------
[Assignment 8, Task 1]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

tree = BST()
values = [1, 2, 3, 4, 5, 6]

for value in values:
    tree.insert(value)

tree2 = BST()
for i in range(1, 7):
    tree2.insert(i)

print(tree.is_valid())
tree._root._right._value = 4
print(tree.is_valid())

print(tree.levelorder())
tree.remove(1)
print(tree.levelorder())
