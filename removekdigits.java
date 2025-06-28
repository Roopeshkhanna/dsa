import java.util.Stack;

public class removekdigits {
    public static void main(String[] args) {
        String num = "0000001432219";
        int k = 3;
        Stack<Character> st = new Stack<>();
        
        // Process each character in the number
        for (char i : num.toCharArray()) {
            while (!st.isEmpty() && k > 0 && st.peek() - '0' > i - '0') {
                st.pop();
                k--;
            }
            st.push(i);
        }
        
        // If there are still digits to remove, pop remaining ones from the stack
        while (k > 0) {
            st.pop();
            k--;
        }
        
        // Build the result from the stack
        String res = "";
        while (!st.isEmpty()) {
            res = st.pop() + res; // Prepend each character to reverse the order
        }
        
        // Remove leading zeros
        int index = 0;
        while (index < res.length() - 1 && res.charAt(index) == '0') {
            index++;
        }
        res = res.substring(index);
        
        System.out.println("Result after removing k digits: " + res);
    }
}
