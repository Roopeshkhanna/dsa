s = "    +042"

ans=''
for i in s:
    if(i==' ' or (i==0 and ans in ('+-'))):
        continue
    elif(i in '+-' and len(ans)==0):
        ans+=i
    elif(i in '0123456789'):
        ans+=i
    else:
        break
if ans == '' or ans in '+-':
    ans = '0'
if(int(ans)<pow(-2,31)):
    print(pow(-2,31))
elif(int(ans)>pow(2,31)-1):
    print(pow(2,31)-1)
else:
    print(int(ans))
       