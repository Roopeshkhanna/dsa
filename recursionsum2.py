def recur(arr,ds,ind,sums,n):
    if(ind>=n):
        if(sum(ds)==sums):
            print(ds)
            return
        
        return
    ds.append(arr[ind])
    recur(arr,ds,ind+1,sums,n)
    ds.pop()
    recur(arr,ds,ind+1,sums,n)
recur([1,2,1],[],0,2,3)