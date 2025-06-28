def subsum(ind,target,arr,dp):
    if(target==0):
        return(True)
    if(ind==0):
        return(arr[0]==target)
    if(dp[ind][target]!=-1):
        return(dp[ind][target])
    
    
    nottake=subsum(ind-1,target,arr,dp)
    take=False
    if(arr[ind]<target):
        take=subsum(ind-1,target-arr[ind],arr,dp)
    dp[ind][target]=take or nottake
    return(dp[ind][target])







arr = [1, 2, 3, 4]
k = 4
n = len(arr)
dp=[[-1 for _ in range(k+1)] for j in range(n)]
print(subsum(n-1,k,arr,dp))