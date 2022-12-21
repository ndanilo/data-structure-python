def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """
    mem = {}
    for elem in lst:
        if elem in mem:
            mem[elem] += 1
        else:
            mem[elem] = 1

    result = []
    if 0 in mem:
        result += [0] * mem[0] 
    if 1 in mem:
        result += [1] * mem[1] 
    if 2 in mem:
        result += [2] * mem[2] 

    # Write your code here!
    return result

lst1 = [2, 0, 0, 1, 2, 1, 0]
lst2 = [2, 1, 1, 1, 2, 1, 1]
lst3 = [2, 2, 0, 2, 2, 2, 0]
lst4 = [2, 0, 0, 0, 2, 0, 0]

print(dutch_national_flag(lst1))
print(dutch_national_flag(lst2))
print(dutch_national_flag(lst3))
print(dutch_national_flag(lst4))