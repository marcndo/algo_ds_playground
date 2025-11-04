def remove_element(nums, val):
    length = len(nums)
    if length == 1 and nums[0] == val:
        return 0
    elif length == 1 and nums[0] != val:
        return 1
    left, right = 0, length - 1
    while left <= right:
        if nums[left] != val:
            left += 1 
        elif nums[right] == val:
            right -= 1
        else:
            nums[left] = nums[right]
            left += 1
            right -= 1
    return left

    

    


        