def pascal(row):
 ans=1
 re=[]
 re.append(1)
 for col in range(1,row):
    ans=ans*(row-col)
    ans//=col
    re.append(ans)
 return(re)
row=6
mre=[]
for i in range(1,row+1):
  mre.append(pascal(i))
print(mre)