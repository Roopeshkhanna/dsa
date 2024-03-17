lis=[1,4,5,7,7,9,7,0,9,8,7,6]
u=int(input("enter num1"))
v=int(input("enter num2"))

k=0
dis=float("inf")
while(True):
    if(lis[k]==u or lis[k]==v):
        ind=k
        break
    k+=1
if(k!=0):
 for i in range(k+1,len(lis)):
    if(lis[ind]==u):
        target=v
    else:
        target=u
    if(lis[i]==lis[ind]):
        ind=i
    elif(lis[i]==target):
        dis=min(dis,i-ind)
        ind=i
print(dis)