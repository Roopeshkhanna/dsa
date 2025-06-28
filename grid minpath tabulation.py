
mat = [[5, 9, 6], [11, 5, 2]]
n = len(mat)
m = len(mat[0])
prev=[0]*m
for i in range(n):
    temp=[0]*m

    for j in range(m):
        if(i==0 and j==0):
            temp[j]=mat[i][j]
        else:
            up=mat[i][j]
            if(i>0):
                up+=prev[j]
            else:
                up=int(1e9)
            left=mat[i][j]
            if(j>0):
                left+=temp[j-1]
            else:
                left=int(1e9)
            temp[j]=min(up,left)
    prev=temp
print(prev[-1])
            