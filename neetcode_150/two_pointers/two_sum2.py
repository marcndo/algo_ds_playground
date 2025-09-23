#Brute for ignoring the sorted aspect, we use double for loops
#get all possible combination of the numbers, add and check if 
#it's equal to the target.

#optimal
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right] 
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return -1
