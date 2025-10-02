def getMoneyAmount(n):
    # 1. Initialize the DP Table
    # We use (n + 1) x (n + 1) for 1-based indexing,
    # and initialize with zeros (our base case).
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 2. Loop for Order of Computation (Bottom-Up)
    # The 'length' loop ensures we solve smaller ranges first.
    for length in range(2, n + 1):
        # 'i' is the start of the range.
        for i in range(1, n - length + 2):
            j = i + length - 1  # 'j' is the end of the range
            
            # 3. Apply the Recurrence Relation (Minimax)
            # Initialize the minimum cost for the current range [i, j] 
            # with a very large number.
            min_cost = float('inf') 
            
            # 'k' is the current guess within the range [i, j]
            for k in range(i, j + 1):
                # Calculate the cost for this guess 'k':
                # cost_if_lower = dp[i][k-1]  (Cost for the left subproblem)
                # cost_if_higher = dp[k+1][j] (Cost for the right subproblem)
                
                # The worst-case subproblem is the MAX of the two resulting costs.
                # Note: The 'if' conditions handle the base case where a subproblem is empty (k-1 < i or k+1 > j), 
                # treating their cost as 0, which is naturally handled if dp is initialized with 0s.
                
                # Calculate the total cost for this guess 'k'
                current_cost = k + max(dp[i][k - 1], dp[k + 1][j])
                
                # Update the MINIMUM cost found so far for the range [i, j]
                min_cost = min(min_cost, current_cost)
            
            # Store the final minimum guaranteed cost for the range [i, j]
            dp[i][j] = min_cost

    # 4. The Final Answer
    # The minimum guaranteed cost for the entire range [1, n]
    return dp[1][n]

print(getMoneyAmount(10))