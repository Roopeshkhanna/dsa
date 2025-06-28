def training(days,last,points,dp):
    if(dp[days][last]!=-1):
        return(dp[days][last])
    if(days==0):
        maxi=0
        for i in range(3):
            if(i!=last):
                maxi=max(maxi,points[days][i])
        return(maxi)
    maxi=0
    for j in range(3):
        if j!=last:
            activity=points[days][j]+training(days-1,j,points,dp)
            maxi=max(activity,maxi)
    dp[days][last]=maxi
    return(dp[days][last])


points = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]

n = len(points)
dp = [[-1 for j in range(4)] for i in range(n)]
print(training(n-1,3,points,dp))