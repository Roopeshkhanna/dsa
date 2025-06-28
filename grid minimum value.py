
def minpath(i,j,dp,mat):
    if(i==0 and j==0):
        return(mat[i][j])
    if(i<0 or j<0):
        return(1e9)
    if(dp[i][j]!=-1):
        return(dp[i][j])
    up=mat[i][j]+minpath(i-1,j,dp,mat)
    left=mat[i][j]+minpath(i,j-1,dp,mat)
    dp[i][j]=min(up,left)
    return(dp[i][j])

mat = [[5, 9, 6], [11, 5, 2]]
n = len(mat)
m = len(mat[0])
dp= [[-1 for j in range(m)] for i in range(n)]
print(minpath(n-1,m-1,dp,mat))

