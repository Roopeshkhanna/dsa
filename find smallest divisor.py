def small(arr,lim):
    low=1
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        sum=0
        for i in arr:
            sum+=ceil(i/mid)
        if(sum>lim):
            low=mid+1
        else:
            high=mid-1
    return(low)






arr = [1, 2, 3, 4, 5]
limit = 8
