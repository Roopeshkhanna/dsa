#brute force
lis = [1, 2, 3, 4, 5, 6, 7]
d = 10
r = d % len(lis)

temp = []
for i in range(r, len(lis)):
    temp.append(lis[i])

for j in range(len(lis) - 1, r - 1, -1):
    lis[j] = lis[j - r]

for k in range(r):
    lis[k] = temp[k]

print(lis)

"""
by slicing
lis=lis[-r:]+lis[:-r]
"""