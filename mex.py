lis=[0,1,5,2]
lis=sorted(lis)
for i in range(0,len(lis)):
    if(lis[i]!=i):
        print(i)
        break
#Time Complexity: O(N * logN)
#Auxiliary Space: O(1)