class tree {
    int data;
    tree left, right;

    tree(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

    tree(int data, tree left, tree right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

public class maxpathsum  {

    public static int height(tree root, int[] sum) {
        if (root == null) return 0;

        int leftsum = Math.max(0,height(root.left, sum));  
        int rightsum = Math.max(0,height(root.right, sum)) ;

        
        sum[0] = Math.max(sum[0], leftsum + rightsum+root.data);

       
        return root.data + Math.max(leftsum, rightsum);
    }

    public static void main(String args[]) {
        tree root = new tree(1);
        root.left = new tree(2);
        root.right = new tree(3);
        root.left.left = new tree(4);
        root.left.right = new tree(5);
        root.left.right.right = new tree(6);
        root.left.right.right.right = new tree(7);

        int[] sum = new int[1]; // To store the diameter
        height(root, sum); // Calculate the height and update diameter
        System.out.print("maxsum of the tree: " + sum[0]);
    }
}
