arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
left=len(arr1)-1
right=0
while(left>=0 and right<len(arr2)):
    if(arr1[left]>arr2[right]):
        arr1[left],arr2[right]=arr2[right],arr1[left]
        left-=1
        right+=1
    else:
        break
arr1.sort()
arr2.sort()
print(arr1,arr2)