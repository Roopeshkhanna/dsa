def path(i,j,dp):

    if(i==0 and j==0):
        return(1)
    if(i<0 or j<0):
        return(0)
    if(dp[i][j]!=-1):
        return(dp[i][j])
    up=path(i-1,j,dp)
    left=path(i,j-1,dp)
    dp[i][j]=up+left
    return(dp[i][j])
m=3
n=2
dp = [[-1 for j in range(n)] for i in range(m)]
print(path(m-1,n-1,dp))
