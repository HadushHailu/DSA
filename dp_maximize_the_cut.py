def maximizeCuts(N, x, y, z):
    # Create a dp array of size N+1 initialized to -1
    dp = [-1] * (N + 1)
    
    # Base case: If length is 0, no cuts are needed
    dp[0] = 0
    
    # Iterate through each length from 1 to N
    for i in range(1, N + 1):
        # Check if the current length can be achieved by making a cut of length x
        if i >= x and dp[i - x] != -1:
            dp[i] = max(dp[i], dp[i - x] + 1)
        # Check if the current length can be achieved by making a cut of length y
        if i >= y and dp[i - y] != -1:
            dp[i] = max(dp[i], dp[i - y] + 1)
        # Check if the current length can be achieved by making a cut of length z
        if i >= z and dp[i - z] != -1:
            dp[i] = max(dp[i], dp[i - z] + 1)
    
    # If dp[N] is still -1, return 0; otherwise, return dp[N]
    return max(0, dp[N])

# Example usage
N = 4
x = 2
y = 1
z = 1
print(maximizeCuts(N, x, y, z))  # Output: 4

