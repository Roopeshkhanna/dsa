strs = "(()())(())(()(()))"
ans = ''
opened = 0

for i in strs:
    if i == '(':
        if opened > 0:
            ans += i
        opened += 1
    if i == ')':
        if opened > 1:
            ans += i
        opened -= 1

print(ans)
