lis = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
presum = 0
k = 3
dic = {}
dic[0] = 1
count = 0

for i in range(len(lis)):
    presum += lis[i]
    if presum - k in dic:
        count += dic[presum - k]
    if presum not in dic:
        dic[presum] = 1
    else:
        dic[presum] += 1

print(count)
#T.C O(nlog(n))
#S.C O(n)