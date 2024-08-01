s = "abaaca"
k = 1

res=0

for i in range(len(s)):
    hash=[0]*26
    dist=0
    for j in range(i,len(s)):
        if(hash[ord(s[j])-97]==0):
            dist+=1
        hash[ord(s[j])-97]+=1
        if(dist==k):
           res+=1
        
print(res)