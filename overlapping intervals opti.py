lis=[[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
lis.sort()
ans=[]
for i in range(len(lis)):
    if(not ans or lis[i][0]>ans[-1][1]):
        ans.append(lis[i])
    else:
        ans[-1][1]=max(lis[i][1],ans[-1][1])
print(ans)
#T.C O(nlog(n)+n)
#S.C O(n)