def recur(ind, arr, ds, target, ans):
    if ind == len(arr):
        if target == 0:
            ans.append(ds[:])
        return
    if arr[ind] <= target:
        ds.append(arr[ind])
        recur(ind, arr, ds, target - arr[ind], ans)
        ds.pop()
    recur(ind + 1, arr, ds, target, ans)

ans = []
recur(0, [2, 2, 3, 7], [], 7, ans)
print(ans)
