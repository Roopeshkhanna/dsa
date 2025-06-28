mat = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
n = len(mat)
m = len(mat[0])
prev=[0]*m
for i in range(n):
    temp=[0]*m
    for j in range(n):
        if(i>0 and j>0 and mat[i][j]==-1):
            temp[j]=0
            continue
        elif(i==0 and j==0):
            temp[j]=1
        else:
            up=0
            left=0
            if(i>0):
                up=prev[j]
            if(j>0):
                left=temp[j-1]
            temp[j]=up+left
    prev=temp

print(prev[m-1])