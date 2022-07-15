inputArray = [1, 1, 1]

def arrayChange(inputArray):
    """You are given an array of integers. On each move you are allowed to
    increase exactly one of its element by one. Find the minimal number of
    moves required to obtain a strictly increasing sequence from the input."""
    sum = 0
    q = inputArray[0]
    for i in inputArray[1:]:
        if i <= q:
            sum += q - i + 1
            q += 1
        else:
            q = i
    return sum


print(arrayChange(inputArray))
