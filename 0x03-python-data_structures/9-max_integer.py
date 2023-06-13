#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_num = my_list[0]
        for num in my_list(len(my_list)):
            if my_list[num] > max_num:
                max_num = my_list[num]
        return max_num
