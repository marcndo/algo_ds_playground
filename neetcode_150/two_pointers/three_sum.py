def three_sum(nums):
    nums.sort()
    n = len(nums)
    if n == 3:
        sub_total = nums[0] + nums[1] + nums[2]
        if sub_total == 0:
            return [nums]
        else:
            return []
    result = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i+1
        right = n-1
        while left < right:
            sub_total = nums[i] + nums[left] + nums[right]
            if sub_total < 0:
                left += 1
            elif sub_total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result