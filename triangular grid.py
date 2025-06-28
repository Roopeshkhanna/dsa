def tripath(i,j,dp,n,triangle):

    if(i==n-1):
        return(triangle[i][j])
    if(dp[i][j]!=-1):
        return(dp[i][j])
    d=triangle[i][j]+tripath(i+1,j,dp,n,triangle)
    dg= triangle[i][j]+tripath(i+1,j+1,dp,n,triangle)
    dp[i][j]=min(d,dg)
    return(dp[i][j])






triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
n = len(triangle)
dp = [[-1 for j in range(n)] for i in range(n)] 
print(tripath(0,0,dp,n,triangle))