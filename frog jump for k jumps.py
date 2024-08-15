def solve(ind, height, dp, k):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    
    minval = float('inf')
    for i in range(1, k+1):
        if ind-i >= 0:
            jump = solve(ind-i, height, dp, k) + abs(height[ind] - height[ind-i])
            minval = min(jump, minval)
    
    dp[ind] = minval
    return dp[ind]

height = [30, 10, 60, 10, 60, 50]
n = len(height)
dp = [-1] * n 
k = 2
print(solve(n-1, height, dp, k))
