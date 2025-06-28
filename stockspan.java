import java.util.Stack;

public class stockspan {
    public static void main(String[] args) {
        int stock[] = {7, 2, 1, 3, 3, 1, 8};  
        int ans[] = new int[stock.length];
        ans[0] = 1;  
        Stack<Integer> st = new Stack<>();
        st.push(0); 
        for (int i = 1; i < stock.length; i++) {
            // Pop elements from the stack while the current stock price is greater
            // than the price at the index stored at the top of the stack
            while (!st.isEmpty() && stock[st.peek()] <= stock[i]) {
                st.pop();
            }
            // Calculate span for the current stock price
            ans[i] = (st.isEmpty()) ? (i + 1) : (i - st.peek());
            // Push current index to stack
            st.push(i);
        }

        
        for (int ch : ans) {
            System.out.println(ch);
        }
    }
}
