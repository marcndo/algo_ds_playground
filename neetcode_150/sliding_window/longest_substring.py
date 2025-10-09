def length_of_longest_substring(s):
    max_length = 0
    length = len(s)
    for i in range(length):
        char_set = set()
        current_count = 0
        for j in range(i, length):
            if s[j]  in char_set:
                break
            else:
                char_set.add(s[j])
                current_count += 1
        max_length = max(max_length, current_count)
    return max_length


def lengthLongestSubstring(s):
    max_length = 0
    left = 0
    char_set = set()
    for right in range(len(s)):
        current_char = s[right]
        while current_char in char_set:
            char_set.remove(current_char)
            left += 1
        char_set.add(current_char)
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    return max_length

    

