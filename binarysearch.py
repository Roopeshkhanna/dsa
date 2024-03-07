def search(arr,low,high,target):
    if(low>high):
        return(-1)
    mid=(low+high)//2
    if(arr[mid]==target):
        return mid
    elif(arr[mid]>target):
        high=mid-1
    elif(arr[mid]<target):
        low=mid+1
    return(search(arr,low,high,target))

lis=[1,2,3,5,7,9]
print(search(lis,0,len(lis)-1,5))
