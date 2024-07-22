def check(arr,minmax):
    k=1
    val=0
    for i in arr:
        if(val+i<=minmax):
            val+=i
        else:
            k+=1
            val=i
    return(k)





def possible(arr,k):
    n=len(arr)
    if(k>n):
        return(-1)
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        num=check(arr,mid)
        if(num<=k):
         high=mid-1
         ans=mid
        else:
            low=mid+1
    return(ans)













boards = [10, 20, 30, 40]
k = int(input("split"))
print(possible(boards,k))
#T.C =n*log(sum()-max())