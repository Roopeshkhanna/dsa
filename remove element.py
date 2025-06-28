lis=[6,2,2,1,3]
def split(lis):
    left=0
    for i in range(len(lis)):
       
        left+=lis[i]
    right=0
    for j in range(len(lis)):
        if(right==(left-lis[j]-right)):
            return(lis[j])
        right+=lis[j]

print(split(lis))


