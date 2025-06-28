
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
public class  heightbalanced {
     


    public static int height(tree root,int level) {
        if(root==null) return 0;
        int left=height(root.left,level);
        if(left==-1) return -1;

        int right=height(root.right,level);
        if (right==-1) return -1;
        if(Math.abs(left-right)>1) return -1;
        return(1+Math.max(left, right));

        
    }

    public static void main(String args[]){
        tree root = new tree(1);
        root.left = new tree(2);
        root.right = new tree(3);
        root.left.left = new tree(4);
        root.left.right = new tree(5);
        
        if(height(root,0)!=-1)
        System.out.print("balanced");
        else    System.out.print("not balanced");
      
      

    }
    
}
