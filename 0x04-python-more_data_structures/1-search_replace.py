#!/usr/bin/python3
"""replaces all occurrences of an element by another in a new lis"""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = []
    for element in my_list:
        new_list.append(replace if element == search else element)
    return new_list

