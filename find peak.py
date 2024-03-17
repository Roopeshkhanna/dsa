def peak(arr,n):
    if(n==1):
        return(0)
    if(arr[0]>arr[1]):
        return(0)
    if(arr[n-1]>arr[n-2]):
        return(n-1)
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2
        if(arr[mid-1]<arr[mid]>arr[mid+1]):
            return(mid)
        elif(arr[mid]>arr[mid-1]):
            low=mid+1
        elif(arr[mid]>arr[mid+1]):
            high=mid-1
        else:
            high=mid-1
lis=[1,2,3,4,5,6,7,8,6,2]
lis2=[1,5,1,2,1]
print(peak((lis),len(lis)))
print(peak((lis2),len(lis2)))