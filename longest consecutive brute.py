lis=[1,1,2,2,3,4,100,101,102,103,104]
#brute
longest=0
for i in range(len(lis)):
    count=1
    x=lis[i]+1
    while(x in lis):#we can use linear search
        x+=1
        count+=1
    longest=max(longest,count)
print(longest)