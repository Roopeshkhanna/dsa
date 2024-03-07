def search(arr,low,high,target):
    ans=0
    mid=(low+high)//2
    if(arr[mid]>=target):
        high=mid-1
        ans=mid
    elif(arr[mid]<target):
        low=mid+1
    search(arr,low,high,target)
    return(ans)
    

    

lis=[1,2,3,5,7,9]
print(search(lis,0,len(lis)-1,4))

"""
Search Insert Position
Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.
If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.
"""