lis=[1,2,3,4,5,6]
#right rotate
#for one element
temp=lis[len(lis)-1]
for i in range(len(lis)-1,0,-1):
    lis[i]=lis[i-1]
lis[0]=temp
print(lis)