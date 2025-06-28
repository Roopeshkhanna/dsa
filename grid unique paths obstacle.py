
def path(i,j,dp,mat):
    if(mat[i][j]==-1 or i<0 or j<0):
        return(0)
    if(i==0 and j==0):
        return(1)
    
    if(dp[i][j]!=-1):
        return(dp[i][j])
    up=path(i-1,j,dp,mat)
    left=path(i,j-1,dp,mat)
    dp[i][j]=up+left
    return(dp[i][j])
mat = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
n = len(mat)
m = len(mat[0])
dp = [[-1 for j in range(m)] for i in range(n)]
print(path(n-1,m-1,dp,mat))