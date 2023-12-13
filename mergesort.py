def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        sort(arr, low, mid)
        sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


lis = [2, 5, 1, 8, 20, 40]
sort(lis, 0, len(lis) - 1)
print(lis)
#T.C o(nlog2(n))
#S.C o(n)