a = [3, 1, 2, 5, 4, 6, 7, 5]
s1=0
s2=0
n=len(a)
s01=(n*(n+1))//2
s02=(n*(n+1)*(2*n+1))//6
for i in a:
    s1+=i
    s2+=i*i
sum=s1-s01
sum2=(s2-s02)//sum
x=(sum+sum2)//2
y=sum2-x
print(x,y)
#T.C O(n)
