mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=4
m=4
for i in range(n-1):
    for j in range(i+1,m):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
for i in range(n):
    mat[i]=list(reversed(mat[i]))
print(mat)
#T.C O(n^2)+(n^2) one for trans and reverse