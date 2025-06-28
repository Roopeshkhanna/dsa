import java.util.*;

class Node {
    int data;
    Node left;
    Node right;

    Node(int val) {
        data = val;
        left = null;
        right = null;
    }
}

public class boundary {

    public static void lefts(Node root, ArrayList<Integer> lis) {
        if (root == null || (root.left == null && root.right == null)) return;
        lis.add(root.data);
        if (root.left != null) {
            lefts(root.left, lis);
        } else if (root.right != null) {
            lefts(root.right, lis);
        }
    }

    public static void rights(Node root, ArrayList<Integer> lis) {
        if (root == null || (root.left == null && root.right == null)) return;
        if (root.right != null) {
            rights(root.right, lis);
        } else if (root.left != null) {
            rights(root.left, lis);
        }
        lis.add(root.data);
    }

    public static void leafs(Node root, ArrayList<Integer> lis) {
        if (root == null) return;
        if (root.left == null && root.right == null) {
            lis.add(root.data);
            return;
        }
        leafs(root.left, lis);
        leafs(root.right, lis);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.right = new Node(6);
        root.left.right.left = new Node(7);
        root.left.right.right = new Node(8);
        root.left.right.left.left = new Node(9);

        ArrayList<Integer> boundary = new ArrayList<>();
        if (root != null) {
            boundary.add(root.data);
        }
        lefts(root.left, boundary);
        leafs(root, boundary);
        ArrayList<Integer> rightBoundary = new ArrayList<>();
        rights(root.right, rightBoundary);
        Collections.reverse(rightBoundary);
        boundary.addAll(rightBoundary);
        System.out.println("Boundary Traversal: " + boundary);
    }
}
