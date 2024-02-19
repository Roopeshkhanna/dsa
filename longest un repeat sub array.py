arr="abcaabcde"
maxi=-1
for i in range(len(arr)):
    dic={}
    for j in range(i,len(arr)):
        if (arr[j] in dic):
            maxi=max(maxi,j-i)
            break
        dic[arr[j]]=1
    else:
        maxi=max(maxi,len(arr)-i)
print(maxi)
            
