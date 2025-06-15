"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/

"""


def is_vowels(a, vowels):
    return a in vowels


vowels = 'aeiou'
def reverse_vowels(s):
    s = list(s)
    n = len(s)
    if n <= 1:
        return s
    i, j = 0,  n - 1
    while i < j:
        while i < j and not is_vowels(s[i], vowels):
            i += 1
        while i < j and not is_vowels(s[j], vowels):
            j -= 1
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)



print(reverse_vowels("IceCreAm"))



