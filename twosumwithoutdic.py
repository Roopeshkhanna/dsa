arr = [2, 3, 6, 5, 8, 4]
target = 14
arr.sort()  # Sort the array in-place

i = 0
j = len(arr) - 1  # Adjust j to point to the last index

while i < j:
    if arr[i] + arr[j] == target:
        print("yes")
        break  # Break out of the loop once you find a pair
    elif arr[i] + arr[j] < target:
        i += 1
    else:
        j -= 1
#if index to be displayed another list to be created so in this case it is  not optimal
#T.C O(N+Nlog(N))