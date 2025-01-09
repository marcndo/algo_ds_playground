"""create a functions that reverse a string
Hi my name is Somebody should be ydobemoS si eman ym iH"""

# A straight forward solution
def reverse_string1(st):
    backward = ''
    if not isinstance(st, str) or not st:
        return f"Double check your input and confirm that it's a string"
    return st[::-1]
    
# A second solution
def reverse_string(st):
    backward = ''
    if not isinstance(st, str) or not st:
        return f"Double check your input and confirm that it's a string"
    elif len(st) < 2:
        backward = st
    for i in range(len(st)-1, -1, -1):
        backward += st[i]
    return backward



print(reverse_string('Hi my name is Somebody'))
print(reverse_string1('Hi my name is Somebody'))