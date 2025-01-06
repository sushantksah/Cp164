"""
-------------------------------------------------------
[Assignment 8, Task 2]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-03-17"
-------------------------------------------------------
"""
# IMPORTS
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total, letter_table

# DATA DICTIONARYS
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

# OPENING STUFF
bst1 = BST()
bst2 = BST()
bst3 = BST()

# FILLING BSTS


def fill_tree(bst, values):
    for i in values:
        var = Letter(i)
        bst.insert(var)

    return


fill_tree(bst1, DATA1)
fill_tree(bst2, DATA2)
fill_tree(bst3, DATA3)

# FILE OPENING
fn = "miserables.txt"
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst1)
t1 = comparison_total(bst1)
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)
fv = open(fn, "r", encoding="utf-8")
do_comparisons(fv, bst3)
t3 = comparison_total(bst3)
print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("{}".format(t1))
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print("{}".format(t2))
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print("{}".format(t3))

letter_table(bst1)
