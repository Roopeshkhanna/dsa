s = "abcde"
goal = "cdeab"
s = "abcde"
goal = "abced"
ans=''
for i in range(len(s)):
    ans=s[i:]+s[:i]
    if(ans==goal):
        print(True)
        break
else:
    print(False)


