
matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
n=len(matrix)
m=len(matrix[0])
prev=matrix[0]
for i in range(1,n):
    temp=[0]*m
    for j in range(m):
        up=matrix[i][j]+prev[j]
        if(j-1>=0):
            left=matrix[i][j]+prev[j-1]
        else:
            left=-int(1e9)
        if(j+1<m):
            right=matrix[i][j]+prev[j+1]
        else:
            right=-int(1e9)
        temp[j]=max(up,left,right)
    prev=temp
            
print(max(prev))