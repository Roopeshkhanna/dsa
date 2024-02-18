lis=[1,2,2,1,1,1,2]
ele=0
count=0
for i in range(len(lis)):
    if(count==0):
        ele=lis[i]
        count=1
    elif(ele==lis[i]):
        count+=1
    else:
        count-=1
count=0
for i in lis:
    if(ele==i):
        count+=1
if(count  > len(lis)//2):
    print(ele)