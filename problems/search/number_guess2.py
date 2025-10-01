def getMoneyAmount(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Loop by length (from 2 up to n)
    for length in range(2, n + 1):
        # i is the start of the range
        for i in range(1, n - length + 2):
            j = i + length - 1  # j is the end of the range
            
            min_cost = float('inf') 
            
            # k is the guess within the range [i, j]
            for k in range(i, j + 1):
                
                # --- FIX FOR INDEX ERROR ---
                
                # Cost of the left subproblem [i, k-1]: If k > i, use dp[i][k-1], otherwise cost is 0.
                cost_if_lower = dp[i][k - 1] if k > i else 0
                
                # Cost of the right subproblem [k+1, j]: If k < j, use dp[k+1][j], otherwise cost is 0.
                cost_if_higher = dp[k + 1][j] if k < j else 0
                
                # The total cost for this guess k (minimax: guess + MAX of subproblems)
                current_cost = k + max(cost_if_lower, cost_if_higher)
                
                # Find the MINIMUM cost across all possible guesses k
                min_cost = min(min_cost, current_cost)
            
            dp[i][j] = min_cost

    return dp[1][n]

print(getMoneyAmount(10))