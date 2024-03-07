def firstoccurence(arr,n,target):
    ans=n
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            high=mid-1
            ans=mid
        else:
            low=mid+1
        
    return(ans)
def lastoccurence(arr,n,target):
    ans=n
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            high=mid-1
            ans=mid
        else:
            low=mid+1
        
    return(ans)
lis=[2, 4, 6, 8, 8, 8, 11, 13]
n=8
target=8
lb=firstoccurence(lis,n,target)
if(lb==n or lis[lb]!=target):
    print([-1,-1])
else:
    up=lastoccurence(lis,n,target)
    print(lb,up-1)
