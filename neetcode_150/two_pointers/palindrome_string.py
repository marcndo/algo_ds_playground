def is_palindrome(strs):
    if len(strs) <= 1:
        return True
    strs_char = ''.join(ch for ch in strs.lower() if ch.isalnum())
    i, j = 0, len(strs_char) - 1
    while i < j:
        if strs_char[i] != strs_char[j]:
            return False
        else: 
            i += 1
            j -= 1
        
    return True