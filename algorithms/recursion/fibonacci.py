# Recursive approach

def recurs_fabonacci(n):
    if n < 2:
        return n
    return recurs_fabonacci(n-1) + recurs_fabonacci(n-2)

# Iterative approach
def iterate_fibonacci(n):
    seq = [0, 1]
    if n < 2:
        return n
    for i in range(2,n+1):
        seq.append(seq[i-1] + seq[i-2])
    return seq[-1]


print(recurs_fabonacci(10))
print(iterate_fibonacci(10))