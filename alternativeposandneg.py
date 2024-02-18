lis=[-1,-2,1,3,-9,0]
#brute approach
pov=[]
neg=[]
for i in lis:
    if(i<0):
        neg.append(i)
    else:
        pov.append(i)
for i in range(len(pov)):
    lis[2*i]=pov[i]
    lis[2*i+1]=neg[i]
print(lis)
#T.C O(n+n/2)
#S.C O(n)
