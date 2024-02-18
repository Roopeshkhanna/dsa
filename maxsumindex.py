lis=[1,-2,3,4,-5,6,7,8]
sum=0
start=0
anstart=0
ansend=0
maxi=float("-inf")
for i in range(len(lis)):
    if(sum==0):
        start=i
    sum+=lis[i]
    if sum>maxi:
        maxi=sum
        anstart=start
        ansend=i
    if(sum<0):
        sum=0
print(anstart,ansend)
#T.C O(n)