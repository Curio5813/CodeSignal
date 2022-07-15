a = []
b = []

def areSimilar(a, b):
    """
    Two arrays are called similar if one can be obtained from another by swapping at
    most one pair of elements in one of the arrays.
    """
    cont = 0
    for k in range(0, len(a)):
        if a[k] != b[k]:
            cont += 1
    a.sort()
    b.sort()
    c = a.copy()
    d = b.copy()
    if 0 <= cont <= 2 and c == d:
        return True
    elif cont > 2 or c != d:
        return False


print(areSimilar(a, b))
