"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-27"
-------------------------------------------------------
"""
# Imports


def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


inp = int(input("num: "))
