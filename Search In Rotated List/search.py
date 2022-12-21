def pivoted_binary_search(lst, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """
    index = 0
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
            index = i
    copy = lst[:]
    copy.sort()
    print(f'copy list: {copy}')
    i = binary_search(copy, 0, len(copy)-1, key)
    if i == -1:
        return -1
    return ((index + i) % len(lst))

def binary_search(lst, i, j,key):
    if i > j:
        return -1

    mid = i + (j-i) // 2

    if lst[mid] == key:
        return mid
    if len(lst) == 1:
        return -1

    if key > lst[mid]:
        return binary_search(lst,mid+1,j, key)
    else:
        return binary_search(lst,i,mid-1, key)

lst = [7, 8, 9, 0, 3, 5, 6]
n = len(lst) #size of the list
key = 3 # Element that is being searched for


lst2 = [1,3,5,6,7,8,9,10,12,13,26,33,34,57]
print(lst)
binary_search(lst2, 0, len(lst2)-1,57)
print(pivoted_binary_search(lst,len(lst),7))