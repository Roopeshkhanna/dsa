a = [1, 2, 3, 0, 1, 1, 1, 3, 1, 2]
dic = dict()
k = 3
leng = 0
sum = 0

for i in range(len(a)):
    sum += a[i]
    if sum == k:
        leng = max(leng, i + 1)
    if sum - k in dic.keys():
        leng = max(leng, i - dic[sum - k] )  
    if sum not in dic.keys():
        dic[sum] = i

print(leng)
