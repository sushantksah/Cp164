"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

# Initalizing Lists
numba1 = Priority_Queue()
numba2 = Priority_Queue()

# Adding les valeus
for value in [1, 1, 1, 11, 13, 3, 34, 4, 5, 5]:
    numba1.insert(value)

for value in [13, 3, 13, 13, 11, 1, 1, 23, 4, 4, 4, ]:
    numba2.insert(value)

# Remove Test
print("Removed value:", numba1.remove())
print()
# Peek Test
print("Peeked value:", numba1.peek())
print()
# Empty Test
print("Is empty?:", numba1.is_empty())
print()
# Length test
print("Length?:", len(numba1))
print()
# Split altt
t1, t2 = numba2.split_alt()
print("t1 after split_alt:", list(t1))
print("t2 after split_alt:", list(t2))
print()
# inserttingg
for value in [5, 10, 15, 20, 25]:
    numba2.insert(value)


key = 20
t3, t4 = numba2.split_key(key)

print("t3 after split_key with key = 20):", list(t3))
print("t4 after split_key (key = 20):", list(t4))
print()
# Comined Pqq
combined_pq = Priority_Queue()
combined_pq.combine(numba1, t4)
print("combined_pq after combining numba1 and target4:", list(combined_pq))
print()
print("Iterating through combined_pq:")
for value in combined_pq:
    print(value)
