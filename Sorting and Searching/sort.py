def intercalate(a,b):
    m = len(b)
    x = len(a)
    v=[0] * (m+x)

    i = 0
    j = 0
    k = 0
    while i < x and j < m:
        if a[i] <= b[j]:
            v[k] = a[i]
            i += 1
        else:
            v[k] = b[j]
            j += 1
        k += 1
    while i < x:
        v[k] = a[i]
        k += 1
        i += 1
    while j < m:
        v[k] = b[j]
        k += 1
        j += 1

    return v

def sort(a):
    L = len(a)
    if L == 1:
        return a

    mid = L // 2
    left = a[:mid]
    right = a[mid:]
    g = sort(left)
    p = sort(right)
    return intercalate(g,p)

x = [3,-5,2,1,10,2,-7,4,5,2,10,-8,11,22,7]

a = [-5,1,4,5,7,8,10]
b = [-3,-2,10,22,30]

v = intercalate(a,b)
print(v)
s = sort(x)
print(s)