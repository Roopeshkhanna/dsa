n=5
for i in range(5):
    for j in range(i):
        print(j+1,end="")
    for k in range(2*(n-i-1)):
        print(" ",end="")
    for m in range(i):
        print(i-m,end="")
    print()
      
    