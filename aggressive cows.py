stalls = [0, 3, 4, 7, 10, 9]
k = 4
stalls.sort()
maxi=max(stalls)
mini=min(stalls)
for i in range(1,maxi-mini):
    cntcows=1
    lastcow=stalls[0]
    for j in range(1,len(stalls)):
        if(stalls[j]-lastcow>=i):
            cntcows+=1
            lastcow=stalls[j]
    if(cntcows<k):
        break
print(i-1)