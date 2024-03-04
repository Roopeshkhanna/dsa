def sorting(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0  
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            count += (mid - left + 1)  
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

    return count


def merge(arr, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2
        count += merge(arr, low, mid)
        count += merge(arr, mid + 1, high)
        count += sorting(arr, low, mid, high)

    return count


lis = [2, 1, 4, 2, 5, 7, 0, 5]
print(merge(lis, 0, len(lis) - 1))
