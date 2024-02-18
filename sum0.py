lis=[]
n=5   
num=n//2
for i in range(num):
            lis.append(num)
            lis.append(-num)
            num-=1
if(n%2!=0):
            lis.append(0)
print(lis,"\n",sum(lis))
#T.C O(n/2)