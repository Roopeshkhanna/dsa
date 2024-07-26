def recur(arr,ds,ind,sums,n):
    if(ind>=3):
        if(sum(ds)==sums):
            print(ds)
            return True
        
        return False
    ds.append(arr[ind])
    if(recur(arr,ds,ind+1,sums,n)== True):
        return(True)
    
    ds.pop()
    if(recur(arr,ds,ind+1,sums,n)== True):
        return(True)
recur([1,2,1],[],0,2,3) 
# to return count of sequence which is equal to sum
"""
def recur(arr,ds,ind,sums,n):
    if(ind>=3):
        if(sum(ds)==sums):#if(sum(ds)>sums) return 0(only for positive to reduce T.C)
            print(ds)
            return 1
        
        return 0
    ds.append(arr[ind])
    l=recur(arr,ds,ind+1,sums,n)
       
    
    ds.pop()
    r=recur(arr,ds,ind+1,sums,n)
    return(l+r)
recur([1,2,1],[],0,2,3) 




"""