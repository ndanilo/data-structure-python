def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """
    return binary_search(lst, 0, len(lst)-1, 0, value)

def binary_search(lst, i, j, reason, key):
    mid = i + (j-i) // 2
    if lst[mid] == key:
        return mid

    if i >= j:
        return mid
    
    if key > lst[mid]:
        return binary_search(lst, mid+1, j, 1, key)
    else:
        return binary_search(lst, i, mid-1, -1, key)


lst = [1, 3, 5, 6]
value = 4

print(search_insert_position(lst, value))