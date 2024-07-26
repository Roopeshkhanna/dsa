def recur(ind, arr, sums, ans):
    if ind >= len(arr):
        ans.append(sums)
        return
    recur(ind + 1, arr, sums + arr[ind], ans)
    recur(ind + 1, arr, sums, ans)

ans = []
recur(0, [3, 1, 2], 0, ans)
ans.sort()
print(ans)
#T.C O(2^n+for sorting 2^nlog(2^n))