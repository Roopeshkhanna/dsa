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

public class diameter {

    public static int height(tree root, int[] diameter) {
        if (root == null) return 0;

        int left = height(root.left, diameter);  // Height of left subtree
        int right = height(root.right, diameter); // Height of right subtree

        // Update the diameter at each node
        diameter[0] = Math.max(diameter[0], left + right);

        // Return the height of the current node
        return 1 + Math.max(left, right);
    }

    public static void main(String args[]) {
        tree root = new tree(1);
        root.left = new tree(2);
        root.right = new tree(3);
        root.left.left = new tree(4);
        root.left.right = new tree(5);
        root.left.right.right = new tree(6);
        root.left.right.right.right = new tree(7);

        int[] diameter = new int[1]; // To store the diameter
        height(root, diameter); // Calculate the height and update diameter
        System.out.print("Diameter of the tree: " + diameter[0]);
    }
}
