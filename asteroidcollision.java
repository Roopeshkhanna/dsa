import java.util.Stack;

public class asteroidcollision {
    public static void main(String args[]) {
        int arr[] = {4, 7, 1, 1, 2, -3, -7,-8};
        Stack<Integer> st = new Stack<>();
        
        for (int num : arr) {
           
            while (!st.isEmpty() && num < 0 && st.peek() > 0) {
                if (Math.abs(num) > st.peek()) {
                    st.pop(); // Current asteroid destroys the top of the stack
                } else if (Math.abs(num) == st.peek()) {
                    st.pop(); // Both asteroids are destroyed
                    num = 0; // Set num to zero to indicate it shouldn't be pushed
                    break;
                } else {
                    // Current asteroid is destroyed; break out of the loop
                    num = 0;
                    break;
                }
            }
            if (num != 0) {
                st.push(num); // Push surviving asteroid
            }
        }
        
        // Collect results in a string to print final stack
        StringBuilder res = new StringBuilder();
        while (!st.isEmpty()) {
            res.insert(0, st.pop() + " ");
        }
        
        System.out.println("Resulting asteroids after collision: " + res.toString().trim());
    }
}
