arr = [2, 3, 6, 5, 8, 4]
target = 14
arr.sort() 

i = 0
j = len(arr) - 1  

while i < j:
    if arr[i] + arr[j] == target:
        print("yes")
        break  
    elif arr[i] + arr[j] < target:
        i += 1
    else:
        j -= 1
#if index to be displayed another list to be created so in this case it is  not optimal
#T.C O(N+Nlog(N))