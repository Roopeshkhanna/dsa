lis=[1,1,1,6,2,2,1,2,2]
n=len(lis)//3
ele1=0
count1=0
ele2=0
count2=0
for i in range(len(lis)):
    if(count1==0 and ele2!=lis[i]):
        ele1=lis[i]
        count1=1
    elif(count2==0 and ele1!=lis[i]):
        ele2=lis[i]
        count2=0
    elif(ele1==lis[i]):
        count1+=1
    elif(ele2==lis[i]):
        count2+=1
    else:
        count1-=1
        count2-=1
print(ele1,ele2)

#T.C O(n)