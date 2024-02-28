from collections import defaultdict
lis=[4,2,2,6,4]
dic= defaultdict(int)
dic[0]=1
xor=0
count=0
k=6

for i in range(len(lis)):
 xor=xor^lis[i]
 x=xor^k
 count+=dic[x]
 dic[xor]+=1
print(count)

 
#T.C O(N) or O(N*logN)
#S.C O(N)