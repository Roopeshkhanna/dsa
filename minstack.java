import java.util.*;
public class minstack {
    public static void main(String[] args) {
        MinStack minStack = new MinStack();

        // Push elements to the stack
        minStack.push(5);
        System.out.println("Pushed 5, Current Min: " + minStack.getMin());  // Expected Min: 5

        minStack.push(3);
        System.out.println("Pushed 3, Current Min: " + minStack.getMin());  // Expected Min: 3

        minStack.push(7);
        System.out.println("Pushed 7, Current Min: " + minStack.getMin());  // Expected Min: 3

        minStack.push(2);
        System.out.println("Pushed 2, Current Min: " + minStack.getMin());  // Expected Min: 2

        // Check the top element
        System.out.println("Top element: " + minStack.top());  // Expected Top: 2

        // Pop elements and check the minimum after each pop
        minStack.pop();
        System.out.println("Popped top, Current Min: " + minStack.getMin());  // Expected Min: 3

        minStack.pop();
        System.out.println("Popped top, Current Min: " + minStack.getMin());  // Expected Min: 3

        minStack.pop();
        System.out.println("Popped top, Current Min: " + minStack.getMin());  // Expected Min: 5

        // Final top element after pops
        System.out.println("Top element: " + minStack.top());  // Expected Top: 5

        // Get the minimum element in the stack
        System.out.println("Minimum element: " + minStack.getMin());  // Expected Min: 5
    }
}


public class MinStack { // Corrected to MinStack
   Stack<Long> st = new Stack<>();
   Long mini;

   // Constructor initializes the mini to the maximum possible value.
   public MinStack(){
       mini = Long.MAX_VALUE;
   }

   // Push operation
   public void push(int val){
       if(st.isEmpty()){
           st.push(Long.valueOf(val));
           mini = Long.valueOf(val);
       } else {
           if(val < mini){
               // Push modified value and update mini
               st.push(2L * val - mini);
               mini = Long.valueOf(val);
           } else {
               st.push(Long.valueOf(val));
           }
       }
   }

   // Pop operation
   public void pop(){
       if(st.isEmpty()) {
           return;
       }
       Long val = st.pop();
       if(val < mini){
           mini = 2 * mini - val; // Restore previous minimum
       }
   }

   // Top operation
   public int top(){
       if(st.isEmpty()) {
           return -1; 
       }
       Long val = st.peek();
       if(val < mini){
           return mini.intValue();
       } else {
           return val.intValue();
       }
   }

   // Get minimum
   public int getMin(){
       return mini.intValue();
   }
}

