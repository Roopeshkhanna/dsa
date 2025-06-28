def getmaxi(i,j,matrix,dp,m):
    if(j<0 or j>=m ):
        return(-int(1e9))
    if(i==0):
        return(matrix[0][j])
    if(dp[i][j]!=-1):
        return(dp[i][j])
    up=matrix[i][j]+getmaxi(i-1,j,matrix,dp,m)
    leftdiag=matrix[i][j]+getmaxi(i-1,j-1,matrix,dp,m)
    rightdiag=matrix[i][j]+getmaxi(i-1,j+1,matrix,dp,m)
    dp[i][j]=max(up,leftdiag,rightdiag)
    return(dp[i][j])

matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
n=len(matrix)
m=len(matrix[0])
dp=[[-1 for _ in range(m)]for h in range(n)]
maxi=float("-inf")
for j in range(m):
    maxi=max(maxi,getmaxi(n-1,j,matrix,dp,m))
print(maxi)