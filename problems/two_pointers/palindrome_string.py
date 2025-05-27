"""
https://leetcode.com/problems/valid-palindrome/description/
Given a string, we have to check if reversing the string
gives the original version after ignoring alphanumeric character
Input: "A man, a plan, a canal: Panama" -> "amanaplanacanalpanama"
Output: True
Convert the string into lower case and removed all alphanumeric character
used two pointers to compare the different characters.
One pointer scans the string from left toward right and the other scans the
string from right towards left and compare both if they are all the same till
left and right pointer are equal, we return true
"""


def is_palindrome(string):
    if len(string) < 1:
        return True
    string_char = ''.join(ch for ch in string.lower() if ch.isalnum())
    print(string_char)
    right_scanner = len(string_char) - 1
    left_scanner = 0
    while left_scanner < right_scanner:
        if string_char[left_scanner] != string_char[right_scanner]:
            return False
        else:
            left_scanner += 1
            right_scanner -= 1
    return True


st = "A man, a plan, a canal: Panama"
st = "0P"
print(is_palindrome(st))
