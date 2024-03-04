lis= [1, 2, -3, 0, -4, -5]
ans=float("-inf")
pre=1
suf=1
for i in range(len(lis)):
    if(pre==0):
        pre=1
    if(suf==0):
        suf=1
    pre=pre*lis[i]
    suf=suf*lis[len(lis)-i-1]
    ans=max(pre,suf)
print(ans)
# T.C O(n)