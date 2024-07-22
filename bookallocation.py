
def check(arr,pages):
    stu=1

    stupage=0
    for i in arr:
        if(stupage+i<=pages):
            stupage+=i
        else:
            stu+=1
            stupage=i
    return(stu)



def findpages(arr,n,m):
    if(n<m):
        return(-1)
    low=max(arr)
    high=sum(arr)#if n is 1 then all books allocated to that student so this is the minimum maximum possible
    while(low<=high):
        mid=(low+high)//2
        stu=check(arr,mid)
        if(stu<=m):
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return(ans)

arr = [25, 46, 28, 49, 24]
n = len(arr)
m = 4
print(findpages(arr,n,m))
#T.C= n*log(sum(arr)-max(arr))