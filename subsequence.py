def recur(ind,arr,ds):
    if(ind>=len(arr)):
        print(ds)
        return
    ds.append(arr[ind])
    recur(ind+1,arr,ds)
    ds.pop()
    recur(ind+1,arr,ds)
    
recur(0,[3,1,2],[])