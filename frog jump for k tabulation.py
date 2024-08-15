height = [30, 10, 60, 10, 60, 50]
n = len(height)
k = 2
dp=[-1]*n
dp[0]=0
for i in range(1,n):
    mini=float('inf')
    for j in range(1,k+1):
        if(i-j>=0):
            jump=dp[i-j]+abs(height[i]-height[i-j])
            mini=min(mini,jump)
    dp[i]=mini
print(dp[n-1])
