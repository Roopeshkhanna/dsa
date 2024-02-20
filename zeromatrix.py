mat=[[1,0,1,1],[0,1,1,1],[0,1,0,1],[1,1,1,1]]
row=4
col=4
col1=1
#rm=[1]*row
#cm=[1]*col
for i in range(row):
    for j in range(col):
        if(mat[i][j]==0):
            mat[i][0]=0
            if j!=0: 
                mat[0][j]=0
            else:
                 col1=0
            
for i in range(1,row):
    for j in range(1,col):
        if(mat[0][j]==0 or mat[i][0]==0):

            mat[i][j]=0
for j in range(col):
    if(mat[0][0]==0):
        mat[0][j]=0
for i in range(row):
    if(col1==0):
        mat[i][0]=0
print(mat)
#T.C O(2n^2)
#S.C O(1)