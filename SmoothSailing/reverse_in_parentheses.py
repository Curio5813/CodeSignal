inputString = '(foo(bar(baz))blim)'


def reverseInParentheses(inputString):
    """Write a function that reverses characters in (possibly nested)
    parentheses in the input string."""
    start = 0
    s = inputString
    print(s)
    for i in range(len(s)):
        if s[i] == '(':
            start = i
        if s[i] == ')':
            end = i
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s


print(reverseInParentheses(inputString))
