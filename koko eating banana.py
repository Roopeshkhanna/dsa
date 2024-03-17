import math

def minban(arr, tot):
    low = 1
    high = max(arr)
   
    while low <= high:
        mid = (low + high) // 2

        time = 0
        for j in arr:
            time += math.ceil(j / mid)
      
        if time > tot:
            low = mid + 1  
        else:
            high = mid - 1
   
    return low

v = [7, 15, 6, 3]
h = 8
print(minban(v, h))
