num = "4106"
n = len(num) - 1

while n >= 0:
    if int(num[n]) % 2 == 1:
        print(num[:n+1])
        break 
    n -= 1
