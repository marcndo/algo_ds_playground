def brute_force(s, k):
    result = 0
    s_len = len(s)
    counter = {} 
    max_freq = 0
    for i in range(s_len):
        for j in range(i, s_len):
            counter[s[j]] = 1 + counter.get(s[j], 0)
            max_freq  = max(max_freq, counter[s[j]])
            if (j - i + 1) - max_freq <= k:
                result = max(result , j - i + 1)
    return result


def longest_repeated_char(s, k):
    l = 0 
    max_freq = 0
    counter = {}
    result = 0
    for r in range(len(s)):
        counter[s[r]] = 1 + counter.get(s[r], 0)
        max_freq = max(max_freq, counter[s[r]])
        while (r - l + 1) - max_freq > k:
            counter[s[l]] -= 1
            l += 1
        result = max(result, (r - l + 1))
    return result
