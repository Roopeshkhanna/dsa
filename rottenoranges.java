import java.util.*;

public class rottenoranges {
    public static int count(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        Queue<int[]> q = new LinkedList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        int fresh = 0;

        // Add all rotten oranges to the queue and count fresh oranges
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    q.add(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        if (fresh == 0) return 0; // No fresh oranges to rot

        int[] x = {0, 0, 1, -1}; // Directions for rows
        int[] y = {1, -1, 0, 0}; // Directions for columns
        int time = 0;
        int rotted = 0; // Count of fresh oranges that have been rotted

        // Process the queue
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] arr = q.poll();
                for (int j = 0; j < 4; j++) {
                    int r = arr[0] + x[j];
                    int c = arr[1] + y[j];

                    // Skip invalid cells or cells that are not fresh oranges
                    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != 1) 
                        continue;

                    // Rot the fresh orange
                    grid[r][c] = 2;
                    q.add(new int[]{r, c});
                    rotted++;
                }
            }
            if (!q.isEmpty()) time++;
        }

        // If all fresh oranges have been rotted, return the time, otherwise return -1
        return (rotted == fresh ? time : -1);
    }

    public static void main(String[] args) {
        int[][] grid = {
            {2, 1, 1},
            {1, 1, 0},
            {0, 1, 1}
        };

        int result = count(grid);
        System.out.println("Time to rot all oranges: " + result);
    }
}
