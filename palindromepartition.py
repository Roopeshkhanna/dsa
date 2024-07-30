def ispalin(s,ind,i):
    return(s[ind:i+1]==s[ind:i+1][::-1])



def solve(ind,s,result,sub):
    if(ind==len(s)):
        result.append(sub[:])
    for i in range(ind,len(s)):
        if(ispalin(s,ind,i)):
            sub.append(s[ind:i+1])
            solve(i+1,s,result,sub)
            sub.pop()
            

result=[]
solve(0,"aabb",result,[])
print(result)