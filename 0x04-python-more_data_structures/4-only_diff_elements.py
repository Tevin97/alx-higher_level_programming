#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = set()

    for ele in set_1:
        if ele not in set_2:
            unique_elements.add(ele)

    for ele in set_2:
        if ele not in set_1:
            unique_elements.add(ele)

    return unique_elements
