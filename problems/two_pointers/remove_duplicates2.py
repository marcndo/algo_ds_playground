def remove_duplicates_brute_force(nums):
    count = {}
    new_nums = []
    for num in nums:
        current_count = count.get(num, 0)
        if current_count < 2:
            new_nums.append(num)
            count[num] = current_count + 1
    return len(new_nums)

def remove_duplicates(nums):
    length = len(nums)
    if length < 2:
        return length
    write = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[write - 2]:
            nums[write] = nums[i]
            write += 1
    return write







nums = [1,1,1,2,2,3]
print(remove_duplicates_brute_force(nums))
print(remove_duplicates(nums))

