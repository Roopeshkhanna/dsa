def allocation(arr,n,m):
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        pages=0
        stu=1
        for i in range(n):
            if(pages+arr[j]<=mid):
                pages+=arr[j]
            else:
                stu+=1
                pages=arr[j]
        if(stu>m):
            low=mid+1
        else:
            high=mid-1
    return(low)


arr = [25, 46, 28, 49, 24]
n = 5
m = 4
print(allocation(arr,n,m))