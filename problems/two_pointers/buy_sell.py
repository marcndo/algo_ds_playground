def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    left = 0
    right = 1
    current_max = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            current_max = max(current_max, profit)
        else:
            left = right
        right += 1
    return current_max


print(max_profit([7, 1, 5, 3, 6, 4]))