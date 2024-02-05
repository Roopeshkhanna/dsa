lis=[1,2,4,5,6]
n=6
xor1=0
xor2=0
for i in range(n-1):
  xor1^=lis[i]
  xor2^=(i+1)
xor2^=n
print(xor1^xor2)
#where 0^0 =0 1^1=0 samenum xor means gives 0
#so xor1 is xor of whole list xor2 is xor for all values from 1 to n
#so xor of xor1 and xor2 give the missing num