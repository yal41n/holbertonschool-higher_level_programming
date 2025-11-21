#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ prints the 1st x elements of a list and only ints """
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            i += 1
            continue
    print()
    return num
