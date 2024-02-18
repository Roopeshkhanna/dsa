lis=[1,-2,3,4,-5,6,7,8]
#better solution
maxi=float("-inf")

for i in range(len(lis)):
    sum=0
    for j in range(i,len(lis)):

       sum+=lis[j]
       maxi=max(maxi,sum)
print(maxi)
#T.C O(n^2)
