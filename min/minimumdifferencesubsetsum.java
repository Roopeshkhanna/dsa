import java.util.ArrayList;
import java.util.Arrays;

public class minimumdifferencesubsetsum {

    public static int subsum(int n, ArrayList<Integer> arr) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr.get(i);
        }

        // DP array to track possible sums
        boolean[][] dp = new boolean[n][sum + 1];

        // Initialize dp array
        for (int i = 0; i < n; i++) {
            dp[i][0] = true;  // sum 0 is always possible
        }
        if (arr.get(0) <= sum) {
            dp[0][arr.get(0)] = true;  // first element can form subset
        }

        // Fill DP table
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= sum; j++) {
                boolean notTake = dp[i - 1][j];
                boolean take = false;
                if (arr.get(i) <= j) {
                    take = dp[i - 1][j - arr.get(i)];
                }
                dp[i][j] = take || notTake;
            }
        }

        // Find minimum difference
        int mini = Integer.MAX_VALUE;
        for (int i = 0; i <= sum / 2; i++) {  // Only go up to half of sum
            if (dp[n - 1][i]) {
                int diff = Math.abs(i - (sum - i));
                mini = Math.min(diff, mini);
            }
        }

        return mini;
    }

    public static void main(String args[]) {
        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 2, 3, 4));
        int n = arr.size();
        System.out.println("The minimum absolute difference is: " + subsum(n, arr));
    }
}
