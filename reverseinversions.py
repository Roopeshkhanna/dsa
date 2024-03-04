def cal(arr,low,mid,high):
    right=mid+1
    count=0
    for i in range(low,mid+1):
        while(right<=high and arr[i]>arr[right]*2):
            right+=1
        count+=right-(mid+1)
    return(count)
def sorting(arr, low, mid, high):
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

    


def merge(arr, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2
        count += merge(arr, low, mid)
        count += merge(arr, mid + 1, high)
        count+=cal(arr, low, mid, high)

        sorting(arr, low, mid, high)

    return count


lis =[4, 1, 2, 3, 1]
print(merge(lis, 0, len(lis) - 1))
#T.C O(logN * (N+N)) = O(2N*logN).