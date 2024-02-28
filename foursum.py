lis=[4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
t=9
ans=set()
find=0
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
      dic=set()
      for k in range(j+1,len(lis)):
         temp=[]
         find=t-(lis[i]+lis[j]+lis[k])
         if find in dic:
            temp=[lis[i],lis[j],lis[k],find]
            temp.sort()
            ans.add(tuple(temp))
         dic.add(lis[k])
print(ans)
# T.C O(N3*log(M))
# S.C O(2 * no. of the quadruplets)+O(N)