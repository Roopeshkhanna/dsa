lis=[2,1,3,4]
for i in range(0,len(lis)-1):
    for j in range(i+1,len(lis)-1):
        if(lis[j]>lis[j+1]):
            lis[j],lis[j+1]=lis[j+1],lis[j]
print(lis)
                   