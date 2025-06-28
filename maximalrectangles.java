import java.util.Arrays;

public class maximalrectangles {
    public static void main(String[] args) {
        int gn[][] = {{1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 0, 0, 1, 0}};

        // Calculating the running sum for each column to create histogram heights
        for (int i = 0; i < gn[0].length; i++) {
            int sum = 0;
            for (int j = 0; j < gn.length; j++) {
                if (gn[j][i] == 0) {
                    sum = 0;  // reset sum when a zero is encountered
                } else {
                    sum += gn[j][i];
                }
                gn[j][i] = sum;
            }
        }

        // Print the modified 2D array
        for (int i = 0; i < gn.length; i++) {
            System.out.println(Arrays.toString(gn[i]));//perform largest rectangle for rach row to find maximal rectangles
        }
    }
}
