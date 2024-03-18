arr = [25, 46, 28, 49, 24]
n = 5
m = 4
maxi=max(arr)
high=sum(arr)
for i in range(maxi,high):
    pages=0
    stu=1
    for j in range(len(arr)):
        if(pages+arr[j]<=i):
            pages+=arr[j]
        else:
            stu+=1
            pages=arr[j]
    if(stu==m):
        print(i)
        break
