"""
-------------------------------------------------------
[Assignment 3, Functions File]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Constants
OPERATORS = "+-*/"

# Functions


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    empty = source1.is_empty() and source2.is_empty()

    i = 1

    while not empty:
        if i % 2 != 0:
            if not source1.is_empty():
                target.push(source1.pop())
            else:
                target.push(source2.pop())
        else:
            if not source2.is_empty():
                target.push(source2.pop())
            else:
                target.push(source1.pop())
        i += 1
        empty = source1.is_empty() and source2.is_empty()

    return target


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    stack = Stack()
    stringl = []

    for i in string:
        if i.isalpha():
            stack.push(i.lower())
            stringl.append(i)

    j = 0

    while not stack.is_empty():
        if stack.pop() != stringl[j].lower():
            palindrome = False

        j += 1

    return palindrome


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = [('Start', [])]  # Stack contains tuples of point and path

    while stack:
        current_point, path = stack.pop()

        # Check if the current point is the exit
        if current_point == 'X':
            return path + ['X']

        # If the point has not been visited yet
        if current_point not in path:
            # Add the point to the path
            path.append(current_point)

            # Add the branches to the stack in reverse order (to explore left branches first)
            branches = maze[current_point]
            for branch in branches:
                stack.append((branch, path.copy()))

    # No exit found
    return None


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    stack = Stack()

    elements = string.split()

    for element in elements:
        if element in OPERATORS:
            right = stack.pop()
            left = stack.pop()

            if element == '+':
                stack.push(left + right)

            elif element == '-':
                stack.push(left - right)

            elif element == '*':
                stack.push(left * right)

            elif element == '/':
                stack.push(left / right)
        else:
            stack.push(float(element))

    answer = stack.pop()

    return answer


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    temp_stack = Stack()

    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())

    return
