from collections import defaultdict

def group_anagram(strs):
    result = defaultdict(list)
    for st in strs:
        sorted_str = str(sorted(st)) # list can not be used as keys in dict
        result[sorted_str].append(st)
    return list(result.values())

# most optimal solution
def group_anagram_(strs):
    result = defaultdict(list)
    for st in strs:
        counter = [0]*26
        for chr in st: # can only run 26 times
            counter[ord(chr) - ord("a")] += 1
        result[tuple(counter)].append(st)
    return list(result.values())


def group_anagram__(sts):
    anagram_groups = {}
    for st in sts:
        st_storted = "".join(sorted(st))
        if  st_storted not in anagram_groups:
            anagram_groups[st_storted] = [st]
        else:
            anagram_groups[st_storted].append(st)
    return list(anagram_groups.values())