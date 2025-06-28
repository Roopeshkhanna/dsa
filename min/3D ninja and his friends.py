def maxchoc(i, j1, j2, m, dp, n, matrix):
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return -int(1e9)  
    
    if i == n - 1:  
        if j1 == j2:
            return matrix[i][j1]
        else:
            return matrix[i][j1] + matrix[i][j2]
        
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    maxi = float("-inf")
   
    
    for dj1 in range(-1, 2):
        for dj2 in range(-1, 2):
            ans = 0
            if j1 == j2:
                ans += matrix[i][j1] + maxchoc(i + 1, j1 + dj1, j2 + dj2, m, dp, n, matrix)
            else:
                ans += matrix[i][j1] + matrix[i][j2] + maxchoc(i + 1, j1 + dj1, j2 + dj2, m, dp, n, matrix)
            maxi = max(maxi, ans)
    
    dp[i][j1][j2] = maxi
    return maxi



matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
n = len(matrix)
m = len(matrix[0])
dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]


print(maxchoc(0, 0, m - 1, m, dp, n, matrix))
