def reverse_words(s):
    if len(s) <= 1:
        return s
    s = s.split()
    left, right = 0, len(s) -1
    while left < right:
        current = s[left]
        s[left] = s[right]
        s[right] = current
        left += 1
        right -= 1
    return " ".join(s)
