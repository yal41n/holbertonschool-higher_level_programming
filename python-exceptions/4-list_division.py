#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ divides element by element 2 lists """
    new_list = []
    for i in range(list_length):
        tmp = 0
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(tmp)
    return (new_list)
