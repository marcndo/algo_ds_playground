
def buy_sell(prices):
    l = max_profit = 0
    for r in range(len(prices)):
        if l == r: # Buying and selling on the same day yield no profit, assuming that price can only update after one day
            continue
        current_profit = prices[r] - prices[l]
        if current_profit < 0:
            l = r
        else:
            max_profit = max(max_profit, current_profit)
    return max_profit
