nums = [4,1,2,1,2]
#just compute xor which will give the odd one
re=nums[0]
for i in range(1,len(nums)):

    re^=nums[i]
print(re)