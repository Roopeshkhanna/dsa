lis = [1, 1, 2, 2, 2, 2, 3, 3, 3,4]
k = 0


for i in range(len(lis)):
    if(lis[i]!=lis[k]):
        k+=1
        lis[k]=lis[i]
        
    
print(k+1)
