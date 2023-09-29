#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""

def find_peak(my_listof_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        my_listof_integers (list): a list of integers
    Returns:
        int: peak(s)
    """
    my_list = my_listof_integers
    # if there is no list of integers return None
    if my_list == []:
        return None
    length = len(my_list)

    zeroth, nth = 0, length - 1
    while zeroth < nth:
        mid = zeroth + (nth - zeroth) // 2
        if my_list[mid] > my_list[mid - 1] and my_list[mid] > my_list[mid + 1]:
            return my_list[mid]
        if my_list[mid - 1] > my_list[mid + 1]:
            nth = mid
        else:
            zeroth = mid + 1
    return my_list[zeroth]
