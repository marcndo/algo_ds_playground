"""https://leetcode.com/problems/reverse-string/: create a functions that reverse a string
Hi my name is Somebody should be ydobemoS si eman ym iH"""


def reverse_string(st):
    if not isinstance(st, list) or not all(isinstance(i, str) and len(i) == 1 for i in st):
        return "double check the input and ensure it's an array of character"
    left, right = 0, len(st) - 1
    while left < right:
        st[left], st[right] = st[right], st[left]
        left += 1
        right -= 1
    return st


print(reverse_string(['A', 'p', 'p', 'l', 'e']))
