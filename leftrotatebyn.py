#brute force
lis=[1,2,3,4,5,6,7]
d=10
r=d%len(lis)
temp=[]
for i in range(r):
   temp.append(lis[i])
for j in range(len(lis)-r):
   lis[j]=lis[r+j]
for k in range(r):
   lis[r+k+1]=temp[k]
print(lis)
