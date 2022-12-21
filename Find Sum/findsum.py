def find_sum(lst, n):
    """
    Add all different values to a set, see if the difference between nth and an element is in the set. 
    If it is, the difference was found
    """
    x = set()
    for elem in lst:
        if n-elem in x:
            return (elem,n-elem)
        else:
            x.add(elem)
    return None
    

lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 21

print(find_sum(lst, n))