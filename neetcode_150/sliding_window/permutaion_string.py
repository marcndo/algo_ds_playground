def check_inclusion(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    if s1_length > s2_length:
        return False
    s1 = sorted(s1)
    for i in range(s2_length):
        for j in range(i, s2_length):
            sub_string = s2[i:j+1]
            if s1 == sorted(sub_string):
                return True
    return False
  

    
def check_inclusion_optimal(s1, s2):
    count1 = {}
    for c in s1:
        count1[c] = 1 + count1.get(c, 0)

    need = len(count1)
    for i in range(len(s2)):
        count2, cur = {}, 0
        for j in range(i, len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)
            if count1.get(s2[j], 0) < count2[s2[j]]:
                break
            if count1.get(s2[j], 0) == count2[s2[j]]:
                cur += 1
            if cur == need:
                return True
    return False


def permutation_string(s1, s2):
    countS1, countS2 = [0] * 26, [0] * 26
    for i in range(len(s1)):
        countS1[ord(s1[i]) - ord('a')]
        countS2[ord(s2[i]) - ord('a')]

    matches = 0
    for i in range(26):
        matches += (1 if countS1[i] == countS2[i] else 0)
    l = 0
    for r in range(len(s1), len(s2)):
      if matches == 26:
         return True

    index = ord(s2[r]) - ord('a')
    countS2[index] += 1
    if countS1[index] == countS2[index]:
         matches += 1
    elif countS1[index] + 1 == countS2[index]:
                matches -= 1

    index = ord(s2[l]) - ord('a')
    countS2[index] -= 1
    if countS1[index] == countS2[index]:
                matches += 1
    elif countS1[index] - 1 == countS2[index]:
         matches -= 1
         l += 1
    return matches == 26

s1 = "abc"
s2 = "lecabee"

print(check_inclusion(s1, s2))
print(check_inclusion_optimal(s1, s2))
print(permutation_string(s1, s2))

