def minw(arr,day):
   low=max(arr)
   high=sum(arr)
   while(low<=high):
      mid=(low+high)//2
      load=0
      days=1

      for i in arr:
         if(load+i>mid):
            days+=1
            load=i
         else:
            load+=i
      if(days>day):
         low=mid+1
      else:
         high=mid-1
   return(low)

    

arr= [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
print(minw(arr,d))
