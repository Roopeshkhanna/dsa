def search(arr,n,target):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==arr[low] and arr[mid]==arr[high]):
            low+=1
            high-=1
            continue
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
arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
n=10
target=3
print(search(arr,n,target))