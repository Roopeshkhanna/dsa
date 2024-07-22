def median(a,b):
    le=len(a)+len(b)
    ind1=le//2
    ind2=ind1-1
    ind1val=-1
    ind2val=-1
    i=0
    j=0
    count=0
    while(i<len(a) and j<len(b) and(ind1val==-1 or ind2val==-1)):
        if(a[i]<b[j]):
            if(count==ind1):
                ind1val=a[i]
            if(count==ind2):
                ind2val=a[i]
            count+=1
            i+=1
        if(a[i]>b[j]):
            if(count==ind1):
                ind1val=b[j]
            if(count==ind2):
                ind2val=b[j]
            count+=1
            j+=1
    while(i<len(a)):
        if(count==ind1):
                ind1val=a[i]
        if(count==ind2):
                ind2val=a[i]
        count+=1
        i+=1
    while(j<len(b)):
         if(count==ind1):
                ind1val=b[j]
         if(count==ind2):
                ind2val=b[j]
         count+=1
         j+=1
    if(le%2==0):
         return((ind1val+ind2val)/2)
    else:
         return(ind1val)








a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print(median(a,b))
#T.C O(n1+n2)