from collections import defaultdict

def beauty(dic):
    maxi=max(dic.values())
    mini=min(dic.values())
    return(maxi-mini)
res=0
s = "aabcb"
s = "aabcbaa"
for i in range(len(s)):
    dic=defaultdict(int)
    for j in range(i,len(s)):
        dic[s[j]]+=1
        res+=beauty(dic)
       
print(res)