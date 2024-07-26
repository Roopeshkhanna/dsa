def permu(arr, ans, maps, ds):
    if len(ds) == len(arr):
        ans.append(ds[:])
        return
    for i in range(len(arr)):
        if not maps[i]:
            ds.append(arr[i])
            maps[i] = True

            permu(arr, ans, maps, ds)

            ds.pop()
            maps[i] = False

arr = [1, 2, 3]
ans = []
maps = [False] * len(arr)
permu(arr, ans, maps, [])
print(ans)
