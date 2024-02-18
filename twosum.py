arr = [2, 3, 6, 5, 8, 4]
target = 14
dic = {}

for i in range(len(arr)):
 
    complement = target - arr[i]
    if complement in dic.keys() :
        print(i, dic[complement])
        break
    dic[arr[i]] = i
