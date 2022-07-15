picture = ['']

def addBorder(picture):
    """
    Given a rectangular matrix of characters, add a border of asterisks(*) to it.
    """
    s, border = '', []
    a = len(picture) + 2
    b = len(picture[0]) + 2
    d = -2
    for k in range(0, a):
        for i in range(0, b):
            n = d + 1
            if k == 0:
                s += '*'
            elif 0 < k < a - 1:
                if i == 0:
                    s += '*'
                elif 0 < i < b - 1:
                    s += picture[n][i - 1]
                elif i == b - 1:
                    s += '*'
            elif k == a - 1:
                s += '*'
            n += 1
        border.append(s)
        s = ''
        d += 1
    return border


print(addBorder(picture))
