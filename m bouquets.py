def bouquets(arr,k,m):
    if(len(arr)<k*m):
        return(-1)
    mini=min(arr)
    maxi=max(arr)
    for i in range(mini,maxi+1):
        cnt=0
        boq=0
        for j in arr:
            if(j<=i):
                cnt+=1
            else:
                boq+=cnt//k
                cnt=0
        boq+=cnt//k
        if(boq>=m):
            return(i)
    return(-1)



arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
print(bouquets(arr,k,m))
