lis=[2,1,5,7,2,5,8,9,33]

for i in range(len(lis)-1,-1,-1):
    swap=0
    for j in range(0,i):
     
      if(lis[j]>lis[j+1]):
            lis[j+1],lis[j]=lis[j],lis[j+1]
            swap+=1
    if(not swap):
        break
print(lis)
#time complexity is o(n^2)
#in best case o(n)
