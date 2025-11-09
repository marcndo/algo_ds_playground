def count_bits(n):
    result = []
    for i in range(n+1):
        count = 0
        while i != 0:
            count += 1
            i &= i - 1
        result.append(count)
    return result
        
