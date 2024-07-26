def permu(num,k):
    nums=[]
    ansstring=''
    fact=1
    for i in range(1,num):
        fact*=i
        nums.append(i)
    nums.append(num)
    k-=1
    while(True):
        ansstring+=str(nums[k//fact])
        del nums[k//fact]
        if(len(nums)==0):
            break
        k%=fact
        fact//=len(nums)


    return(ansstring)
print(permu(4,17))
#T.C O(n^2)
#S.C O(n)