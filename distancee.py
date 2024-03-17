lis = [1, 4, 5, 7, 7, 9, 7, 0, 9, 8, 7, 6]
dic = {}
u = 7
v = 1
dis = float("inf")
for i in range(len(lis)):
    dic[lis[i]] = i
    if lis[i] == u:
        if v in dic:
            dis = min(dis, i - dic[v])
    elif lis[i] == v:
        if u in dic:
            dis = min(dis, i - dic[u])

print(dis)
