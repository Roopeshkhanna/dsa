a = [3, 1, 2, 5, 4, 6, 7, 5]
xr=0

for i in range(len(a)):
    xr=xr^a[i]
    xr=xr^[i+1]
bitno=0
while(1):#to find differentiating bit
    if(xr & (1<<bitno)):
        break
    else:
        bitno+=1

one=0
zero=0
for i in range(len(a)):
    if(a[i](1<<bitno)):
        one=one^a[i]
    else:
        zero^=a[i]
    if(i+1(1<<bitno)):
        one^=i+1
    else:
        zero^=i+1

print(one,zero)