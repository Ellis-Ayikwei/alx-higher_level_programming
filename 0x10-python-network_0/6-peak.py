#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    middle_element = size
    middle_position= size // 2

    if size == 0:
        return None

    while True:
        middle_element = middle_element // 2
        if (middle_position< size - 1 and
                list_of_integers[mid] < list_of_integers[middle_position+ 1]):
            if middle_element // 2 == 0:
                middle_element = 2
            middle_position= middle_position+ middle_element // 2
        elif middle_element > 0 and list_of_integers[mid] < list_of_integers[middle_position- 1]:
            if middle_element // 2 == 0:
                middle_element = 2
            middle_position= middle_position- middle_element // 2
        else:
            return list_of_integers[mid]
