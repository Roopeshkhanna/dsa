
triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
n = len(triangle)

front=triangle[n-1]
for i in range(n-2,-1,-1):
    curr=[0]*n
    for j in range(i,-1,-1):
        d=triangle[i][j]+front[j]
        dg=triangle[i][j]+front[j+1]
        curr[j]=min(d,dg)
    front=curr
print(front[0])