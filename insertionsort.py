lis=[2,12,3,44,7,2,0]
for i in range(0,len(lis)):
    j=i
    while(lis[j-1]>lis[j] and j>0):
        lis[j-1],lis[j]=lis[j],lis[j-1]
        j-=1
print(lis)
#time complexity o[n^2]
#best o[n]