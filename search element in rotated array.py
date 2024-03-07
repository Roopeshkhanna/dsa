def search(arr,n,target):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return(mid)
        if(arr[low]<=arr[mid]):
            if(arr[low]<=target<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        else:
            if(arr[mid]<=target<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return(-1)
arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
n = 9
target=1
print(search(arr,n,target))