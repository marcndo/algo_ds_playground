def group_anagrams(strs):
    anagrams = {}
    for st in strs:
        s_sorted = "".join(sorted(st))
        if s_sorted not in anagrams:
            anagrams[s_sorted] = [st]
        else:
            anagrams[s_sorted].append(st)
    return anagrams


def groupAnagrams(strs):
    anagrams ={}
    for st in strs:
        count = [0] * 26
        for char in st:
            count[ord(char) - ord('a')] += 1
        count_tuple = tuple(count)
        # check if key not in dict, initialize it, defaultdict could be a better option
        if count_tuple not in anagrams:
            anagrams[count_tuple] = []
        anagrams[count_tuple].append(st)
    return list(anagrams.values())