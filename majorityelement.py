arr=[1,1,2,3,4,1,1,1,1]
count=0
element=arr[0]
for i in range(len(arr)):
   
    if(count==0):
        element=arr[i]
        count=1
    else:
         if(arr[i]==element):
           count+=1
         else:
           count-=1

for i in arr:
   if(i==element):
      count+=1
if(count>len(arr)//2):
   print(element)
#T.C O(N)+O(N)