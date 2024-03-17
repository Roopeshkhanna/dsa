def val(mid, n, num):
    val = 1
    for i in range(1, n + 1):
        val = val * mid
        
        if val > num:
            return 2
    if(val==num):
        return(1)
    return 0

def root(num, n):
    low = 1
    high = num
    while low <= high:
        mid = (low + high) // 2
        cal = val(mid, n, num)
        if cal == 1:
            return mid
        elif cal == 2:  
            high = mid - 1
        else:
            low = mid + 1
    return (-1)

print(root(64, 3))






