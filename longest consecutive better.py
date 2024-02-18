lis=[1,1,2,2,3,4,100,101,102,103,104]
longest=1
#first sort so O(Nlog(N))
lis.sort()
last=float('-inf')
count=0
for i in range(len(lis)):
    if(lis[i]-1==last):
        last=lis[i]
        count+=1
    elif(lis[i]!=last):
        count=1
        last=lis[i]
    longest=max(longest,count)
print(longest)
#T.C O(nlogn+n)
    


