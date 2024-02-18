lis=[-1,-2,1,3,-9,0]
pos=0
neg=1
re=[0]*len(lis)
for i in lis:
    if(i<0):
        re[neg]=i
        neg+=2
    else:
        re[pos]=i
        pos+=2
print(re)
#T.C O(n)
#S.C O(n)