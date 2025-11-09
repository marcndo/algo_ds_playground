def single_non_duplicates(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

