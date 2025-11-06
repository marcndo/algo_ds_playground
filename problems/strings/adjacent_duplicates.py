def adjacent_duplicates(s):
    stack = []
    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
 
    return "".join(stack)



s = "abbaca"
print(adjacent_duplicates(s))



