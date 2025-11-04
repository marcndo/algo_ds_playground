def reverse_word(s):
    result = []
    for word in s.split(" "):
        char_arr = list(word)
        length = len(word)
        i, j = 0, length - 1
        
        word = [0] * length
        while i < j:
            char_arr[i], char_arr[j] = char_arr[j], char_arr[i]
            i += 1
            j -= 1
        result.append("".join(char_arr))
    return " ".join(result)

