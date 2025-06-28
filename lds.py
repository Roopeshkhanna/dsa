lis=[9,4,3,2,5,4,3,1]
lds=[1]*len(lis)
max=0
max_ind=0
prevind=[-1]*len(lis)
ans=[]
for i in range(len(lis)):
    for j in range(i):
        if(lis[i]<lis[j] and lds[i]<lds[j]+1):
            lds[i]=lds[j]+1
            prevind[i]=j
for i in range(len(lis)):
        if (max < lds[i]):
            max = lds[i]
            max_ind=i
currentind=max_ind

while(currentind!=-1):
     ans.append(lis[currentind])
     currentind=prevind[currentind]

     
     
print(max)
ans.reverse()
print(ans)