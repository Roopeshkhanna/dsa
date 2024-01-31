def quicksort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quicksort(arr, low, partition_index)
        quicksort(arr, partition_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:#here i must be less than high 
            i += 1                         #since i is incremented here
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[low] = arr[low], arr[j]
    return j

arr = [2, 1, 4, 6, 8]
quicksort(arr, 0, 4)
print(arr)
#Time complexity O(nlog(n))
#space complexity O(1)





