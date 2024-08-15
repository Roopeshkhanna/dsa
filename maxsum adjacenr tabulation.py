arr = [2, 1, 4, 9]
n = len(arr)
dp=[-1]*n
dp[0]=arr[0]
for i  in range(1,n):
    pick=arr[i]
    if(i>1):
        pick+=dp[i-2]
    notpick=0+dp[i-1]
    maxi=max(pick,notpick)
    dp[i]=maxi
print(dp[n-1])

"""
less space




# Function to solve the problem of finding the maximum sum of non-adjacent elements in an array
def solve(n, arr):
    # Initialize variables to keep track of the previous maximum and the one before that
    prev = arr[0]  # Initialize with the first element of the array
    prev2 = 0      # Initialize with 0 because there is no element before the first
    
    # Loop through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum value when picking the current element
        pick = arr[i]
        
        # Check if there are at least two elements before the current element
        if i > 1:
            pick += prev2
        
        # Calculate the maximum value when not picking the current element
        non_pick = 0 + prev
        
        # Calculate the maximum value for the current index
        cur_i = max(pick, non_pick)
        
        # Update the 'prev' and 'prev2' variables for the next iteration
        prev2 = prev
        prev = cur_i
    
    # Return the maximum value for the last index, which represents the solution
    return prev

# Main function to test the code
def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    
    # Call the solve function and print the result
    print(solve(n, arr))

if __name__ == "__main__":
    main()


"""