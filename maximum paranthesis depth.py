s = "()(())((()()))"
s = "(1)+((2))+(((3)))"
open=0
ans=0
for i in s:
    if(i=='('):
        open+=1
        if(open>ans):
            ans=open
    elif(i==')'):
        open-=1
print(ans)