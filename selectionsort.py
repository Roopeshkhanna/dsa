lis = [3, 1, 9, 6, 0, 4]

for i in range(0, len(lis) - 1):
    mini = i
    for j in range(i, len(lis)):
        if lis[mini] > lis[j]:
            mini = j
    lis[i], lis[mini] = lis[mini], lis[i]

print(lis)
