
def find_in_rotated_array(nums, target):
    length = len(nums) - 1
    left , right = 0, length
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(find_in_rotated_array([4,5,6,7,0,1,2], 1))


