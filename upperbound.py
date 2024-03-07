def upperbound(arr,low,high,target):
    
  ans=0
  while(low<=high):
       

    mid=(low+high)//2
    if(arr[mid]>target):
        high=mid-1
        ans=mid
    elif(arr[mid]<=target):
        low=mid+1
  return(ans)
    

    

lis=[3, 5, 8, 9, 15, 19]
print(upperbound(lis,0,len(lis)-1,9))
