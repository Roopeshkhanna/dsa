s = "      a good          example      "
ans = ''
temp = ''

for i in s:
    if i != ' ':
        temp += i
    elif temp and i==' ':
        ans = temp + ' ' + ans
        temp = ''


if temp:
    ans = temp + ' ' + ans


ans = ans.strip()

print(ans)
