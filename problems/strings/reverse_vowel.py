def reverse_vowels(s):
    s = list(s)
    n = len(s)
    vowels = set('aeiouAEIOU')
    if n <= 1:
        return s
    i, j = 0,  n - 1
    while i < j:
        while i < j and s[i] not in vowels:
            i += 1
        while i < j and s[j] not in vowels:
            j -= 1
        if i == j:
            continue
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)




