#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers
    Returns: peak of list_of_integers or None
    """
    if list_of_integers == []:
        return None
    if len(list_of_integers) <= 2:
        return max(list_of_integers)  # Handle small lists directly

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
