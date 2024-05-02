#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in an unsorted list using binary search.

    Args:
        list_of_integers(int): list of integers

    Returns: peak of list_of_integers or None
    """

    size = len(list_of_integers)
    if size == 0:
        return None
    peak = binary_search(list_of_integers, 0, size - 1)
    return list_of_integers[peak]


def binary_search(a, left, right):
    """Recursive binary search of the peak"""
    if left >= right:
        return left
    mid = ((right - left) // 2) + left
    if a[mid] > a[mid + 1]:
        return binary_search(a, left, mid)
    else:
        return binary_search(a, mid + 1, right)
