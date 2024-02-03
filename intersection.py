a=[1,1,2,3,4,8]
b=[1,1,1,2,2,5,7,8]
n1 = len(a)
n2 = len(b)
inter= []

i = 0
j = 0
while(i<n1 and j<n2):
    if(a[i]<b[j]):
        i+=1
    elif(b[j]<a[i]):
        j+=1
    else:
        inter.append(a[i])
        i+=1
        j+=1
print(inter)
