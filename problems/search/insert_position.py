def search_insert_position(nums, target):
    if not nums:
        return 0
    left, right = - 1, len(nums)
    while left + 1 < right:
        mid  = (left + (right - left)) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right

nums = [1,3,5,6]
target = 7

print(search_insert_position(nums, target))