def product_except_self__(nums):
    length  = len(nums)
    result = [1] * length
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result[i] = product
    return result
# We could also calculate the prefix and suffix products and just multiply corresponding enteries


def product_except_self(nums):
    length = len(nums)
    answer = [1] * length
    prefix_prod = 1
    for i in range(length):
        answer[i] = prefix_prod
        prefix_prod = answer[i] * nums[i] 
    suffix_prod = 1
    for j in range(length - 1, -1, -1):
        answer[j] = answer[j] * suffix_prod
        suffix_prod = suffix_prod * nums[j]
    return  answer
    


print(product_except_self([1, 4, 9, 3]))
print(product_except_self([1, 4, 9, 3]))
