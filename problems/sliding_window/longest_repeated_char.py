from collections import defaultdict


def character_replacement(s, k):
    count = defaultdict(int)
    max_freq = 0
    left = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(character_replacement("AABABBA", k = 1))