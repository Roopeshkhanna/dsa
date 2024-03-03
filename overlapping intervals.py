lis=[[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
lis.sort()
ans=[]
for i in range(len(lis)):
    start=lis[i][0]
    end=lis[i][1]

    if ans and end<=ans[-1][1]:
        continue
    for j in range(i+1,len(lis)):
        if(lis[j][0]<=end):
            end=max(end,lis[j][1])
        else:
            break
    ans.append([start,end])
print(ans)     
#T.C O(nlog(n)+2n)
#S.C O(n)
