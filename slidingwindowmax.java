import java.util.*;
public class slidingwindowmax {
    public static int[] windowmax(int arr[],int k){

        int ans[]=new int[arr.length-k+1];
        int ind=0;
        Deque<Integer> q =new ArrayDeque<>() ;
        
            
        
        for(int i=0;i<arr.length;i++){
            if(!q.isEmpty() && q.peekFirst()==i-k){
                q.pollFirst();

            }
            while(!q.isEmpty()&& arr[q.peekLast()]<=arr[i]){
                q.pollLast();
            }
            q.offerLast(i);
            if(i>=k-1){
                ans[ind++]=arr[q.peekFirst()];
            }

        }
  return(ans);



            }
    public static void main(String[] args) {
        int arr[]={4,0,-1,3,5,3,6,8};
        int k=3;
        for(int ch:windowmax(arr, k)){
            System.err.println(ch);
        }

    }
}
