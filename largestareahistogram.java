import java.util.Stack;

public class largestareahistogram {
    public static void main(String[] args) {
        int histo[] = {3, 1, 5, 6, 2, 3};
        int ans = 0, n = histo.length;
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && histo[st.peek()] > histo[i]) {
                int ele = st.pop();
                int pse = st.isEmpty() ? -1 : st.peek();  // previous smaller element index
                int width = i - pse - 1;
                ans = Math.max(ans, histo[ele] * width);
            }
            st.push(i);
        }

        // Calculating area for remaining elements in stack
        while (!st.isEmpty()) {
            int ele = st.pop();
            int pse = st.isEmpty() ? -1 : st.peek();  // previous smaller element index
            int width = n - pse - 1;
            ans = Math.max(ans, histo[ele] * width);
        }

        System.out.println("Largest area in histogram: " + ans);
    }
}
