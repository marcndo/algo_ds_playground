
"""
Goal: Reverse only the vowels in a given string.
Input: s = "hello"
Output: "holle"
input: "welcome"
output: welcome
input s = "Isah"

invariance: We only swap when we've found a vowel from the left and from the right
State: All vowels before i have already been swapped
"""


def swap_vowels(s):
    s = list(s)
    i = 0
    j = len(s) - 1
    vowels = "aeiou"
    while i < j and s[i] not in vowels:
        i += 1
    while i < j and s[j] not in vowels:
        j -= 1
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
    return "".join(s)


s = "hello"
s1 = "welcome"
s2 = "azi"
s3 = "cook"
s4 = "shokolokobagoshie"
test_case = [s, s1, s2, s3, s4]

for case in test_case:
    print("=========word=========")
    print(case)
    print("=========output=========")
    print(swap_vowels(case))
