lis = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
t = 9
ans = []
lis.sort()

for i in range(len(lis)):
    if i > 0 and lis[i] == lis[i - 1]:
        continue
    for j in range(i + 1, len(lis)):
        if j > i + 1 and lis[j] == lis[j - 1]:
            continue
        k = j + 1
        l = len(lis) - 1
        while k < l:
            summ = lis[i] + lis[j] + lis[k] + lis[l]
            if summ > t:
                l -= 1
            elif summ < t:
                k += 1
            else:
                ans.append([lis[i], lis[j], lis[k], lis[l]])
                k += 1
                l -= 1
                while k < l and lis[k] == lis[k - 1]:
                    k += 1
                while k < l and lis[l] == lis[l + 1]:
                    l -= 1

print(ans)
#T.C O(n^3)