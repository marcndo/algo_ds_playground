"""
Given a string s containing just the characters '(', ')',
 '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
I will use a stack to store the open characters. For each close character i will compare if the
character in the head of the stack matches it corresponding close character then pop it
"""

def is_valid(st):
    n = len(st)
    if n <= 1:
        return False
    char_list = []
    i = 0
    while i < n:
        if st[i] in '([{':
            char_list.append(st[i])
        elif st[i] in ')]}':
            top_char = char_list[-1]
            if (st[i] == ')' and top_char == '(') or \
                (st[i] == ']' and top_char == '[') or \
                    (st[i] == '}' and top_char == '{'):
                char_list.pop()
            return False
        i += 1
    return len(char_list) == 0


# def is_valid(st):
#     n = len(st)
#     if n <= 1:
#         return False
#
#     char_list = []  # stack to keep track of opening brackets
#     i = 0
#     while i < n:
#         if st[i] in '([{':
#             char_list.append(st[i])
#         elif st[i] in ')]}':
#             # Check if stack is empty before trying to match
#             if not char_list:
#                 return False
#             top = char_list[-1]
#             if (st[i] == ')' and top == '(') or \
#                (st[i] == ']' and top == '[') or \
#                (st[i] == '}' and top == '{'):
#                 char_list.pop()
#             else:
#                 return False
#         i += 1
#
#     # If stack is empty, all brackets matched properly
#     return len(char_list) == 0


print(is_valid("()[]{}"))

