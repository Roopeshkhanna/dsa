public class partitionequalsubsetsum {
    public static boolean subsum(int n, int target, boolean dp[][], int arr[]) {
        // Initialize dp array
        for (int i = 0; i < n; i++) {
            dp[i][0] = true;  // Sum 0 is always possible by selecting no elements
        }
        if (arr[0] <= target) {
            dp[0][arr[0]] = true;  // First element can form a subset if within target
        }

        // Filling dp table
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= target; j++) {
                boolean notTake = dp[i - 1][j];  // Exclude current element
                boolean take = false;
                if (arr[i] <= j) {  // Include current element if it's <= current sum j
                    take = dp[i - 1][j - arr[i]];
                }
                dp[i][j] = take || notTake;  // Either include or exclude the current element
            }
        }

        return dp[n - 1][target];  // Return whether it's possible to get sum 'target'
    }

    public static void main(String args[]) {
        int arr[] = {2, 3, 3, 3, 4, 5};
        int n = arr.length;
        int sum = 0;

        // Calculate total sum of array
        for (int a : arr) {
            sum += a;
        }

        // If the total sum is odd, it's not possible to partition it into two equal subsets
        if (sum % 2 != 0) {
            System.out.println("False");
        } else {
            boolean dp[][] = new boolean[n][(sum / 2) + 1];  // DP table for subset sum
            boolean ans = subsum(n, sum / 2, dp, arr);  // Check if we can form sum/2
            System.out.println(ans);
        }
    }
}
