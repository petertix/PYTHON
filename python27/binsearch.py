#!/usr/bin/python
"""
    This program performs a Binary Search of a List
"""


def binsearch(mylist, item):
    """ This is the Binary search Function """

    found = False
    first = 0
    last = len(mylist) + 1

    while first < last and not found:
        mid = (first + last)//2
        print('mid = %d  mylist[mid] = %d ' % (mid, mylist[mid]))
        if mylist[mid] == item:
            found = True
        else:
            if item < mylist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


if __name__ == '__main__':

    MYLIST = [1, 3, 5, 6, 7, 11, 23, 34, 35, 47, 56, 78, 89, 100]

    targetValue = input('Enter an Integer to search for in the list: ')

    print(binsearch(MYLIST, targetValue))
