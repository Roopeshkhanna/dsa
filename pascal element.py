#formula ncr
def ncr(n,r):
    re=1
    r-=1
    n-=1
    for i in range(r):
        re=re*(n-i)
        re=re//(i+1)
    return(re)
print(ncr(5,3))
#T.C O(column-1)
