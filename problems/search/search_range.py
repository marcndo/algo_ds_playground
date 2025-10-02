def search_range(nums, target):
    length = len(nums)
    if not nums:
        return [-1, -1]
    
    def first_occurence(nums,target):
        left, right = 0, length - 1
        first_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_idx = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_idx
    
    def last_occurence(nums, target):
        left, right = 0, length - 1
        last_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_idx = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid - 1
            else:
                right = mid - 1
        return last_idx

    
    return [first_occurence(nums,target), last_occurence(nums,target)]

nums = [5,7,7,8,8,10]
target = 8
print(search_range(nums, target))