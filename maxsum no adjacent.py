def solve(ind,arr,dp):
    if(dp[ind]!=-1):
        return(dp[ind])
    if(ind==0):
        return(arr[ind])
    if(ind <0):
        return(0)
    pick=arr[ind]+solve(ind-2,arr,dp)
    notpick=0+solve(ind-1,arr,dp)
    dp[ind]=max(pick,notpick)
    return(dp[ind])
    




arr = [2, 1, 4, 9]
n = len(arr)
dp=[-1]*n
print(solve(n-1,arr,dp))
