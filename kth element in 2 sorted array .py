def kth(a,b,n1,n2,k):
    if(n1>n2):
        return(kth(b,a,n2,n1,k))
    low=max(0,k-n2)
    high=min(k,n1)
    while(low<=high):
        mid1=(low+high)//2
        mid2=k-mid1
        l1,l2,r1,r2=float('-inf'),float('-inf'),float('inf'),float("inf")
        
        if(mid1<n1):
            r1=a[mid1]
        if(mid2<n2):
            r2=b[mid2]
        if(mid1>=0):
            l1=a[mid1-1]
        if(mid2>=0):
            l2=b[mid2-1]
        if(l1<r2 and l2<r1):
            return(max(l1,l2))
        elif(l1>r2):
          high=mid1-1
        else:
            low=mid1+1
lis1=[1,2,3,6,9]
lis2=[5,6,7,8,10]
k=7
print(kth(lis1,lis2,len(lis1),len(lis2),k))








            
            
