s = "babad"
def palin(left ,right):
    while(left>=0 and right<len(s) and s[left]==s[right]):
        left-=1
        right+=1
    return(s[left+1:right])
ans=s[0]
for i in range(len(s)):
    odd=palin(i,i)
    even=palin(i,i+1)
    if(len(odd)>len(ans)):
        ans=odd
    if(len(even)>len(even)):
        ans=even
print(ans)


