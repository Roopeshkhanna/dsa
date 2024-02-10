a = [1, 2, 8, 0, 1, 1, 1, 3, 1, 2]
leng = 0
k = 3
sum = 0
left = 0
right = 0

while right < len(a):
    sum += a[right]
    while sum > k and left <= right:
        sum -= a[left]
        left += 1
    if sum == k:
        leng = max(leng, right - left + 1)
    right += 1

print(leng)
