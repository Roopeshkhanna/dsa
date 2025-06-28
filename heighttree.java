
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
public class  heighttree {
     


    public static int height(tree root,int level) {
        if(root==null) return 0;
        int right=height(root.left,level);
        int left=height(root.right,level);
        return(1+Math.max(left, right));

        
    }

    public static void main(String args[]){
        tree root = new tree(1);
        root.left = new tree(2);
        root.right = new tree(3);
        root.left.left = new tree(4);
        root.left.right = new tree(5);
        root.left.right.right = new tree(6);
        root.left.right.right.right = new tree(7);

        System.out.print(height(root,0));

    }
    
}
