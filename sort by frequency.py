from collections import defaultdict
dic=defaultdict(int)
s = "tree"
s = "cccaaa"
s = "Aabb"

for i in s:
    dic[i]+=1
dic=sorted(dic.items(),key=lambda item:item[1],reverse=True)
ans=''
for i in dic:
    ans+=i[0]*i[1]
print(ans)
