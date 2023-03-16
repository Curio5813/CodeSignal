from csv import reader
from math import sqrt, exp


def stringToFloat():
    """
    This function open .csv values and return a list or float numbers.
    :return:
    """
    arq = open("problem034.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l1[i][k] = float(l1[i][k])
    return l1


def binarySearch(l1):
    """
    This function take a list as parameter from the function above and
    calculate the Binary Search. It's the name of the simple and efficient
    algorithm for finding a position where Monotonic Function reaches
    the given value. Monotonic Function means that its values steadily grow
    with growing argument.

    Formula to Binary Search:

            A * x + B * sqrt(x ^ 3) - C * exp(-x / 50) - D = 0

    :param l1:
    :return:
    """
    low, high, guess, asw, asw2 = 0, 100, 1, [], []
    for i in range(0, len(l1)):
        while guess != 0:
            x = (low + high) / 2
            guess = l1[i][0] * x + l1[i][1] * sqrt(x ** 3) - l1[i][2] * exp(-x / 50) - l1[i][3]
            if guess > 0:
                high = x - 1
            elif guess < 0:
                low = x + 1
            asw.append(x)
            if len(asw) >= 30:
                asw2.append(asw[-1])
                break
        low, high, asw = 0, 100, []
    return print(*asw2)


binarySearch(stringToFloat())
