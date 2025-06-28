public class trappingrainwater {
    public static void main(String[] args) {
        int height[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        int leftmax = 0, rightmax = 0;
        int l = 0, r = height.length - 1, ans = 0;

        while (l <= r) {
            if (height[l] <= height[r]) {
                if (height[l] >= leftmax) {
                    leftmax = height[l];
                } else {
                    ans += leftmax - height[l];
                }
                l++;
            } else {
                if (height[r] >= rightmax) {
                    rightmax = height[r];
                } else {
                    ans += rightmax - height[r];
                }
                r--;
            }
        }

        System.out.println("Total water trapped: " + ans);  // Expected output: 6
    }
}
