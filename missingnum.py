
arr=[1,3,4,5]
n=5
sum=0
sumr=n*(n+1)//2
for i in arr:
    sum+=i
print(sumr-sum)
#if negative num present not possible
#if sum greater then long long data type must be used