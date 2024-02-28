lis = [-1, 0, 1, 2, -1, -4]
k = 0
se = set()

for i in range(len(lis)):
    dic = {}
    for j in range(i + 1, len(lis)):
        rou = []
        find = k - (lis[i] + lis[j])
        if find in dic:
            rou.extend([lis[i], lis[j], find])
            rou.sort()
            se.add(tuple(rou))
        dic[lis[j]] = j

print(se)
#T.C O(N^2 log(m))
#S.C O(n->dic)+(no of triplets *2)
