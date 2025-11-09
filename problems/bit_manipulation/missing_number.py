def missing_number(nums):
    n = len(nums)
    nums = set(nums)
    for num in range(n+1):
        if num not in nums:
            return num 

#We use the XOR councellation rule (X ^ X = 0, X ^0 = X) 
def missing_number_optimal(nums):
    n = len(nums)
    missing = n
    for i in range(n):
        missing ^= nums[i]
        missing ^= i
    return missing


    
nums = [0, 1, 2, 3, 5, 6, 7]
print(missing_number(nums))
print(missing_number_optimal(nums))
