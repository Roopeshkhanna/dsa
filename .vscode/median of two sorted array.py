def median(a,b):
    n1,n2=len(a),len(b)
    if(n1>n2):
        return(median(b,a))
    n=n1+n2
    left=(n1+n2+1)//2
    high=n1 #high=min(left,n1)
            #low=max(0,left-n2)
    low=0
    while(low<=high):
        mid1=(low+high)//2
        mid2=left-mid1
        l1,l2,r1,r2=float('-inf'),float('-inf'),float('inf'),float(' inf')
        if(mid1<n1):
            r1=a[mid1]
        if(mid2<n2):
            r2=b[mid2]
        if(mid1-1>=0):
            l1=a[mid1-1]
        if(mid2-1>=0):
            l2=b[mid2-1]
        if(l1<=r2 and l2<=r1):
            if(n%2==1):
                return(max(l1,l2))
            else:
                return((float(max(l1,l2))+float(min(r1,r2)))//2.0)
        elif(l1>r2):
            high=mid1-1
        else:
            low=mid1+1

        

        




a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print(median(a,b))

