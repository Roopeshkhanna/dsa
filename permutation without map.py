def permu(ind,arr,ans):
    if(ind==len(arr)):
        ans.append(arr[:])
        return
    for i in range(ind,len(arr)):
        arr[ind],arr[i]=arr[i],arr[ind]
        permu(ind+1,arr,ans)
        arr[ind],arr[i]=arr[i],arr[ind]
ans=[]
permu(0,[1,2,3],ans)
print(ans)