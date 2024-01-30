lis=[2,1,5,7,2,5,8,9,33]
swap=0
for i in range(len(lis)):
    for j in range(1,len(lis)-i):
        if(lis[j]<lis[j-1]):
             swap+=1
             lis[j-1],lis[j]=lis[j],lis[j-1]
    if(swap==0):
      break
print(lis)
//Time complexity o(n^2) 
//space complexity o(1)
