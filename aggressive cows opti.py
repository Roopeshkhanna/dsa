def possible(arr,dist,cows):
    cntcows=1
    lastcow=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]-lastcow>=dist):
            cntcows+=1
            lastcow=arr[i]
    if(cntcows<cows):
        return(0)
    return(1)
def dis(arr,k):
    n=len(arr)
    arr.sort()
    low=1
    high=arr[n-1]-arr[0]
    while(low<=high):
        mid=(low+high)//2
        if(possible(arr,mid,k)):
            low=mid+1
        else:
            high=mid-1
    return(high)
stalls = [0, 3, 4, 7, 10, 9]
k = 4
print(dis(stalls,k))
