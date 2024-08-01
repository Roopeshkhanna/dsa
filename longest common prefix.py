strs = ["flower", "flow", "flight"]
strs.sort()
ans = ''
i = 0




while  strs[0][i] == strs[-1][i]:
    ans += strs[0][i]
    i += 1

print(ans)
