"""
-------------------------------------------------------
[Utilities]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    for value in range(len(source)):
        stack.push(source.pop())

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while stack.is_empty() == False:
        target.append(stack.pop())

    target.reverse()

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    stack = Stack()
    print(f"is_empty expects True: {stack.is_empty()}")
    print(f"push: {source[0]}")
    stack.push(source[0])
    print(f"is_empty expects False: {stack.is_empty()}")
    print(f"peek expects 5: {stack.peek()}")
    stack.pop()


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while queue.is_empty() == False:
        target.append(queue.peek())
        queue.remove()

    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print(f"Test for is_empty = True: {q.is_empty()}")

    # tests for the queue methods go here
    for i in a:
        q.insert(i)

    print(f"Test for is_empty = False: {q.is_empty()}")

    print(f"Test for Length: {len(q)}")

    print(f"Test for Peek: {q.peek()}")

    while q.is_empty() == False:
        print(f"Test for Remove: {q.remove()}")

    print(f"Test for is_empty = True: {q.is_empty()}")

    # print the results of the method calls and verify by hand

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not pq.is_empty():
        target.append(pq.remove())

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    # tests for the priority queue methods go here
    pq = Priority_Queue()

    print("Testing insert and is_empty:")
    for item in a:
        pq.insert(item)
        print(f"Inserted {item}, Queue is_empty: {pq.is_empty()}")

    print("\nTesting peek and remove:")
    while not pq.is_empty():
        print(f"Peek: {pq.peek()}, Removed: {pq.remove()}")

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        llist.prepend(source.pop())

    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in llist:
        target.append(value)

    llist._values.clear()

    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print("the list should be empty", lst.is_empty())
    lst.append(source[0])

    print("is empty false now:", lst.is_empty())
    print()
    print("append and peek the value", lst.peek())
    print()

    lst.append(source[1])
    lst.insert(0, source[2])
    print("insert a food at index 0")
    print()
    for v in lst:
        print(v)
    print()
    print("What is the max?", lst.max())
    print()
    print("What is the min?", lst.min())
    print()

    key = Food("Spring rolls wrong", 2, True, 653)
    print("find any instances spring rolls wrong:")
    print("does it contain key?", key in lst)
    print("how many times?", lst.count(key))

    r = lst.remove(key)
    print("remove spring rolls wrong", r)
    print()
    lst[1] = Food("Poutine", 0, False, 710)
    hmm = lst[0]
    print("update the list at index 1")
    print("the first variable in the list is", hmm)

    for v in lst:
        print(v)
    n = lst.index(Food("Poutine", 0, False, 710))
    print("the index Poutine is", n)
    print()
    print("finding Poutine...")
    print(lst.find(Food("Poutine", 1, False, 66)))

    return
