n=5
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end="")
    for k in range((2*i)+1):
        print("*",end="")
    print()

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(((4-i)*2)+1,0,-1):
        print("*",end="")
    
    print()