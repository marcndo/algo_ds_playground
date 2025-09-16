def is_anagram_(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    def count_string(st):
        count = {}
        for chr in st:
            count[chr] = count.get(chr, 0) + 1
        return count
    return count_string(s) == count_string(t)


def is_anagram__(s,t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True
