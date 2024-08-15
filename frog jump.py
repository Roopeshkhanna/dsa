def jump(ind, height,dp):
    if ind == 0:
        return 0
    if(dp[ind]!=-1):
        return(dp[ind])
    jumptwo=float('inf')
    jumpone = jump(ind - 1, height,dp) + abs(height[ind] - height[ind - 1])
    if ind > 1:
        jumptwo = jump(ind - 2, height,dp) + abs(height[ind] - height[ind - 2])
    return(min(jumpone,jumptwo))

height = [30, 10, 60, 10, 60, 50]
n = len(height)
dp = [-1] * n
print(jump(len(height) - 1, height,dp))
