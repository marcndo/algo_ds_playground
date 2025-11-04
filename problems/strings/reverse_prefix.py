def reverse_prefix(word, ch):
    if len(word) == 1:
        return word 
    idx = word.index(ch)
    print(idx)
    word = list(word)
    i, j = 0, idx
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    return "".join(word)

    
    