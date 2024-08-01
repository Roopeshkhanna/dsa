s = "a good          example"
ans = []
temp = ''


for i in range(len(s)):
    ch = s[i]
    if ch != ' ':  
        temp += ch
    elif temp:  
        ans.append(temp)
        temp = ''


if temp:
    ans.append(temp)


strans = ''
while ans:
    strans += ans.pop() + ' '


strans = strans.strip()

print(strans)
