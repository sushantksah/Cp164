"""
-------------------------------------------------------
[Assignment 3, Task 5]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

# Test Tuple
palindrome_tests = [
    "racecar",
    "Otto",
    "Able was I ere I saw Elba",
    "A man, a plan, a canal, Panama!",
    "SUSHANT KUMAR SAH",
    "12321"]

# Loop to test
for test in palindrome_tests:
    result = is_palindrome_stack(test)
    print(f"'{test}' is a palindrome: {result}")
