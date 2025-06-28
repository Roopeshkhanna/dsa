# You are using Python
n=int(input())
lis=list(map(int,input().split()))
ans=0

cnt=0
j=0
if(len(lis)==1):
    print(1)
else:
    while(j<len(lis)-1):
        if(lis[j]<lis[j+1]):
            break
        j+=1
    
    prev=lis[j]
    for i in range(j,n-1):
        if i==n-2 or (lis[i]<prev and lis[i]<lis[i+1]):
            
            if(i==n-2 and lis[i]>lis[i+1]):
                cnt+=1
            ans=max(ans,cnt+1)
       
            cnt=1
            
        else:
            cnt+=1
            
    
        prev=lis[i]
    

    ans=max(cnt,ans)
    print(ans)
            
        
    