import java.util.*;
class NGEC{
    public static void main(String[] args) {
        
    
    Stack <Integer> stack=new Stack<>();
    int arr[]={5,7,1,2,6,0};
    int n=arr.length;
    int nge[]=new int[n];
    for(int i=2*n-1;i>=0;i--){
        while(stack.isEmpty()==false && stack.peek()<=arr[i%n]){
            stack.pop();
        }
        if(i<n){
            if(stack.isEmpty()==true){
                nge[i]=-1;
            }
            else{
                nge[i]=stack.peek();
            }
        }
        stack.push(arr[i%n]);
    }
    for (int i: nge)
    System.out.println(i);
    }
}