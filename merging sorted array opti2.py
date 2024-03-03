import math as p

def swap(arr1, arr2, ind1, ind2):
  if ind1 < len(arr1) and ind2 < len(arr2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
n = len(arr1)
m = len(arr2)
gap = p.ceil((n + m) / 2)

while gap > 0:
    left = 0
    right = left + gap
    while right < n + m:
        if left < n and right >= n: 
            swap(arr1, arr2, left, right - n)
        elif left >= n:
            swap(arr2, arr2, left - n, right - n)
        else:
            swap(arr1, arr2, left, right)
        left += 1
        right += 1
    if gap == 1:
        break
    gap = p.ceil(gap // 2)
        
print(arr1, arr2)
#T.C O((n+m)*log(n+m))
#S.C O(1)