mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=4
m=4
mat2=[[0 for x in range(n)]for y in range(m)]
for i in range(n):
    for j in range(m):
        mat1[n-1-i][j]=mat[i][j]
print(mat2)
#T.C O(n^2)
#S.C O(n^2)
