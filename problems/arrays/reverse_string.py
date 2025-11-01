def reverse_string(s):
    l , r = 0, len(s) - 1
    while l < r:
        current = s[l]
        s[l] = s[r]
        s[r] = current
        l += 1
        r -= 1
    return s


s = ["h","e","l","l","o"]
s = reverse_string(s)
print(s)