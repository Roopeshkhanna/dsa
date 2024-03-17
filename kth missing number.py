def missing(arr,k,n):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        missing=arr[mid]-(mid+1)
        if(missing<k):
            low=mid+1
        else:
            high=mid-1
    return(low+k)

    

arr= [4, 7, 9, 10]
k = 4
n=len(arr)
print(missing(arr,k,n))
