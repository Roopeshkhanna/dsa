lis=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
#array to be sorted
t=0
ans=[]
for i in range(len(lis)):
    if(i>0 and lis[i]==lis[i-1]):
        continue
    j=i+1
    k=len(lis)-1
    while(j<k):
        sum=lis[i]+lis[j]+lis[k]
        if(sum<t):
            j+=1
        elif(sum>t):
            k-=1
        else:
            ans.append([lis[i],lis[j],lis[k]])
            j+=1
            k-=1
            while(lis[j]==lis[j-1]):
                j+=1
            while(lis[k]==lis[k+1]):
                k-=1
print(ans)

#T.C O(nlog(n)->sorting)+(n^2)
#S.C O(1)

