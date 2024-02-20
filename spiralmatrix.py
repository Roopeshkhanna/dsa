mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=4
m=4
top=0
bottom=n-1
left=0
right=m-1
while(top<=bottom and left<=right):


 for i in range(left,right+1,1):
     print(mat[top][i])
 top+=1
 for j in range(top,bottom+1):
    print(mat[j][right])
 right-=1
 if(top<=bottom):
  for k in range(right,left-1,-1):
   print(mat[bottom][k])
 bottom-=1
 if(left<=right):
  for  t in range(bottom,top-1,-1):
   print(mat[t][left])
 left+=1

#T.C(n*m)