def equalStacks(h1, h2, h3):
    # Write your code here
    sum1=sum(h1)
    sum2=sum(h2)
    sum3=sum(h3)
    while(sum1!=sum2 or sum2!=sum3 or sum1!=sum3):
        mins=min(sum1,sum2,sum3)
        
        if(sum1>mins):
            sum1-=h1.pop(0)
        elif(sum2>mins):
           sum2-=h2.pop(0)
        else:
            sum3-=h3.pop(0)        
    return(sum1)
h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]
print(equalStacks(h1,h2,h3))