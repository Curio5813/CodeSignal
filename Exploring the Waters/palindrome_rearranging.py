from itertools import permutations

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"

def palindromeRearranging(inputString):
    """Given a string, find out if its characters can be rearranged to form a palindrome."""
    permutacao = []
    valor = False
    for i in range(0, len(inputString) + 1):
        permutacao = list("".join(k) for k in permutations(inputString, i))
    print(permutacao)
    for k in range(0, len(permutacao)):
        if permutacao[k] == permutacao[k][::-1]:
            valor = True
    return valor


print(palindromeRearranging(inputString))
