n=int(input())
lis=list(map(int,input().split()))
rec=set()
for i in lis:
    rec.add(i)
    mex=0
   
    while(mex in rec):
        mex+=1
    print(mex,end=' ')
    