
def dist(arr,k):
    gap=[0]*(len(arr)-1)
    for i in range(1,k+1):
        dist=-1
        ind=-1
        

        for j in range(len(arr)-1):
            diff=arr[j+1]-arr[j]
            actualdist=diff/(gap[j]+1)
            if(actualdist>=dist):

                dist=actualdist
                ind=j
        gap[ind]+=1
    maxdist=-1
    for j in range(len(arr)-1):
        diff=(arr[j+1]-arr[j])/(gap[j]+1)
        
        if(maxdist<diff):
            maxdist=diff
    return(maxdist)
            



          

arr = [1, 2, 3, 4, 5]
k = 4
print(dist(arr,k))
#T.C O(k*n) + O(n)
#S.C O(n-1)