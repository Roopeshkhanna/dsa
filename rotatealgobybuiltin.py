def reverse(arr, start, end):
    arr[start:end] = arr[start:end][::-1]
    return arr

lis = [1, 2, 3, 4, 5, 6, 7]
d = 10
d = d % len(lis)
lis = reverse(lis, 0, d)
lis = reverse(lis, d, len(lis))
lis = reverse(lis, 0, len(lis))
print(lis)
