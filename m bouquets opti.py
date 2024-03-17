def bouquets(arr,k,m):
    if(len(arr)<k*m):
        return(-1)
    low=min(arr)
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        cnt=0
        boq=0
        for j in arr:
            if(j<=mid):
                cnt+=1
            else:
                boq+=cnt//k
                cnt=0
        boq+=cnt//k
        if(boq>=m):
            high=mid-1
        else:
            low=mid+1
        
    return(low)



arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
print(bouquets(arr,k,m))
