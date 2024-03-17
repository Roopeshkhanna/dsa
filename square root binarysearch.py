def sqroot(num):
    low=0
    high=num
    while(low<=high):
       mid=(low+high)//2
       if(mid*mid<=num):
           low=mid+1
       else:
           high=mid-1

       
           
          
    return(high)
print(sqroot(66))
