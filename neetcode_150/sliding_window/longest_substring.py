def lengthLongestSubstring(s):
    max_length = 0
    for i in range(len(s)):
        char_set = set()
        for j in range(i, len(s)):
            current_char = s[j]
            if current_char in char_set:
                break
            else:
                char_set.add(current_char)
            current_length = j - i + 1
        max_length = max(max_length, current_length)
    return max_length


def length_of_longest_substring(s):
    l = 0                 
    max_length = 0        
    char_set = set()      
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        
        current_length = r - l + 1
        
        max_length = max(max_length, current_length)
    return max_length

s = "zxyzxyz"
print(lengthLongestSubstring(s))
print(length_of_longest_substring(s))