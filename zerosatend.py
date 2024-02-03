lis=[0,1,3,6,2,0,0,0,0,0,0,7,0,4]
j=-1

for i in range(len(lis)):
    if(lis[i]==0):

        j=i
        break
if(j>=0):
 for i in range(j+1,len(lis)):
    if(lis[i]!=0):
        lis[i],lis[j]=lis[j],lis[i]
        j+=1
print(lis)