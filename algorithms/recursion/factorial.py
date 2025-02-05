# Recursive approach

def recursive_factorial(n):
    if n < 2:
        return 1
    return n * recursive_factorial(n-1)


# Iterative approach
def iterate_factorial(n):
    factorial = 1
    if n < 2:
        return 1
    for i in range(2, n+1):
        factorial *=i
    return factorial



print(recursive_factorial(0))
print(iterate_factorial(0))