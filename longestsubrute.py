a=[1,2,3,1,1,1,2,1]
leng=0
s=3
for i in range(len(a)):
    sum=0
    for j in range(i,len(a)):
       
       
        sum+=a[j]
        if(sum==3):
            leng=max(leng,j-i+1)
print(leng)
#T.C O(n^2)
#S.C O(1)
