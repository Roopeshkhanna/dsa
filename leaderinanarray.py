#optimal
lis=[1,22,24,5,6,3]
re=[]
maxi=float("-inf")
for i in range(len(lis)-1,-1,-1):
    
    if(lis[i]>maxi):
        maxi=lis[i]
        re.append(lis[i])
re.sort()
print(re)
#T.C O(N)+ if to sort O(N)
#S.C O(N)
