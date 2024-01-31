n = int(input())
lis =list(map(int,input().split()))
maxi = 0

for i in range(0, n):  # Corrected the loop condition
    sums = 0
    s = 0
    inde = n - i
    k = 1
    c=i
    
    while s < inde:  # Corrected the loop condition
        for j in range(0, k):
            sums += lis[c]
            inde -= 1
            s += 1
            c+=1
        k += 1
    if maxi < sums:
            maxi = sums

print(maxi)
