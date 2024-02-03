a=[1,1,2,3,4,8]
b=[1,1,1,2,2,5,7]
n1 = len(a)
n2 = len(b)
uni = []

i = 0
j = 0
while i < n1 and j < n2:
        if a[i] <= b[j]:
            if not uni or uni[-1] != a[i]:
                uni.append(a[i])
            i += 1
        else:
            if not uni or uni[-1] != b[j]:
                uni.append(b[j])
            j += 1

while i < n1:
        if not uni or uni[-1] != a[i]:
            uni.append(a[i])
        i += 1

while j < n2:
        if not uni or uni[-1] != b[j]:
            uni.append(b[j])
        j += 1

    
print(uni)