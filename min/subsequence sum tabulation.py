
arr = [1, 2, 3, 4]
k = 4
n = len(arr)
dp=[[-1 for _ in range(k+1)]for h in range(n)]
for i in range(1,n):
    dp[i][0]=True
if(arr[0]<=k):
    dp[0][arr[0]]=True
for i in range(1,n):
    for target in range(1,k+1):
        nottake=dp[i-1][target]
        take=False
        if(arr[i]<=target):
            take=dp[i-1][target-arr[i]]
        dp[i][target]=take or nottake
print(dp[n-1][k])