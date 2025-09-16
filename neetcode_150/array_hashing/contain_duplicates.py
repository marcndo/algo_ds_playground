def has_duplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def has_duplicates_(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

def has_duplicates__(nums):
    hash_set = set()
    for element in nums:
        if element in hash_set:
            return True
        hash_set.add(element)
    return False

def has_duplicates___(nums):
    return False if len(set(nums)) == len(nums) else True

print(has_duplicates(nums = [1, 2, 3, 3]))
print(has_duplicates_(nums = [1, 2, 3, 3]))
print(has_duplicates__(nums = [1, 2, 3, 3]))
print(has_duplicates___(nums = [1, 2, 3, 3]))