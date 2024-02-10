a=[1,2,3,1,1,1,1,2,1]
leng=0
s=3
for i in range(len(a)):
    for j in range(i,len(a)):
        sum=0
        for k in range(i,j+1):
            sum+=a[k]
        if(sum==3):
            leng=max(leng,j-i+1)
print(leng)
#T.C O(n^3)
#S.C O(1)