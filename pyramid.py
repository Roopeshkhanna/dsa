n=5
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end="")
    for k in range((2*i)+1):
        print("*",end="")
    print()
