lis=[1,-2,3,4,-5,6,7,8]
sum=0
maxi=float("-inf")
for i in range(len(lis)):
    sum+=lis[i]
    if sum>maxi:
        maxi=sum
    if(sum<0):
        sum=0
print(maxi)
#T.C O(n)