height = [30, 10, 60, 10, 60, 50]
dp=[-1]*len(height)
dp[0]=0
for ind in range(1,len(height)):
    jump2=float('inf')
    jump1=dp[ind-1]+abs(height[ind]-height[ind-1])
    if ind>1:
        jump2=dp[ind-2]+abs(height[ind]-height[ind-2])
    dp[ind]=min(jump1,jump2)


print(dp[len(height)-1])

#To optimize space
"""

height = [30, 10, 60, 10, 60, 50]

prev1=0
prev2=0
for ind in range(1,len(height)):
    jump2=float('inf')
    jump1=prev1+abs(height[ind]-height[ind-1])
    if ind>1:
        jump2=prev2+abs(height[ind]-height[ind-2])
    curr=min(jump1,jump2)
    prev2=prev1
    prev1=curr
print(prev1)




"""