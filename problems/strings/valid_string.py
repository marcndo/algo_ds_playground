"""
Test the validity of a string.
Given an input string made up of only the following '(', '{' '['
')', '}', ']', determine if a given string is valid or not.
A string is valid if each opening character has a corresponding closing character
Each open character is close in the same order in which it was opened

Input: string
output: True or False
Given a string you want me to check is it is valid or not base on the conditions above

input: s = '()[]{}'
output: True
input: s = '{[()]}'
output: True
input: []
output: True
input: s = '(]){}'
output: False

I will use a stack to store the characters as they're being accessed
in the string if it one of the character '({[' as soon as i encounter a different
character, i compare it with the head of the stack if it's the complement of one of the characters
'({[' i pop it from the stack and return true if all the characters are popped

FUNCTION valid_character(s)
    n = string_length
    IF n == 1 AND s[0] not in '({['
        RETURN False
    ELSE IF n == 0
        RETURN True
    stack = []
    FOR i in s
        IF s[i] in '({['
            push s[i] to stack
        ELSE
        current_character = s[i]
            IF (current_character == '{' AND stack.peak() == '{') or \
                  (current_character == '[' AND stack.peak() == ']') or \
                     (current_character == '(' AND stack.peak() == ')')
            stack.pop()
        ELSE
            RETURN FALSE

    RETURN len(stack) == 0
"""


def is_valid_character(s):
    n = len(s)
    if n == 1 and s[0] not in '({[':
        return False
    elif n == 0:
        return True
    stack = []
    for i in range(n):
        if s[i] in '({[':
            stack.append(s[i])
        else:
            current_character = s[i]
            if len(stack) != 0:
                head = stack[-1]
                if current_character in ')}]':
                    if ((head == '{' and current_character == '}') or
                       (head == '[' and current_character == ']') or
                       (head == '(' and current_character == ')')):
                        stack.pop()
    return len(stack) == 0
# '(]){}'

s = '()[]{}'
s1 = '{[()]}'
s2 = []
s3 = '(]){}'
s4 = '%(){}'
s5 = '](){}'
print(is_valid_character(s3))
# cases = [s, s1, s2, s3, s4, s5]
# for case in cases:
#     print("===Test input===")
#     print(case)
#     print("===Test Result===")
#     print(is_valid_character(case))
