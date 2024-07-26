def recur(ind, arr, ans, ds):
    ans.append(ds[:])
    for i in range(ind, len(arr)):
        if i != ind and arr[i] == arr[i - 1]:
            continue
        ds.append(arr[i])
        recur(i + 1, arr, ans, ds)
        ds.pop()
    return

arr = [1,1,2, 2,2,3]
arr.sort()
ans = [] 
recur(0, arr, ans, [])
print(ans)
print(len(ans))
