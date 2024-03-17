def minsearch(arr,n):
    low=0
    high=n-1
    ans=float("inf")
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[high]):
            ans=min(ans,arr[low])
        if(arr[low]<=arr[mid]):
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[high])
            high=mid-1
    return(ans)
lis=[4, 5, 6, 7, 0, 1, 2, 3]
print(minsearch(lis,len(lis)))