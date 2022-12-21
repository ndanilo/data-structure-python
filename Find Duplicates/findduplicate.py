def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """
    mem = {}

    for elem in lst:
        if elem not in mem:
            mem[elem] = 1
        else:
            mem[elem] += 1

    result = [ x for x in mem if mem[x] > 1 ]  # A list to store duplicates
    return result

lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
print(find_duplicates(lst))