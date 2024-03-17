import math as p

def minban(arr,tot):
   
   
   for i in range(1,max(arr)):
      time=0
      for j in (arr):
         time+=p.ceil(j/i)
      if(time<=tot):
         return(i)
v = [7, 15, 6, 3]
h = 8
print(minban(v,h))
         
         
