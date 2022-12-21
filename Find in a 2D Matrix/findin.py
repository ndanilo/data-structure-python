def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """
    for row in lst:
        if number <= row[-1]:
            return binary_search(row, 0, len(row)-1, number)

    return False

def binary_search(lst, i, j, key):
    mid = i + (j-i) // 2
    if lst[mid] == key:
        return True

    if i > j:
        return False

    if key > lst[mid]:
        return binary_search(lst,mid+1,j,key)
    else:
        return binary_search(lst, i, mid-1, key)

list_2d  =[[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]
number = 10

print(find_in(list_2d, number))