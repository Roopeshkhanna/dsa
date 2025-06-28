import java.util.*;

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
class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() {
        return key;
    }

    public void setKey(K key) {
        this.key = key;
    }

    public V getValue() {
        return value;
    }

    public void setValue(V value) {
        this.value = value;
    }
}

class preorder {

    // Create tree from level order array
    public static tree levelorder(int[] arr) {
        if (arr.length == 0) {
            return null;
        }
        Queue<tree> q = new LinkedList<>();
        tree root = new tree(arr[0]);
        q.add(root);
        for (int i = 1; i < arr.length; i++) {
            tree cur = q.poll();
            if (arr[i] > 0) {
                cur.left = new tree(arr[i]);
                q.add(cur.left);
            }
            if (++i < arr.length && arr[i] > 0) {
                cur.right = new tree(arr[i]);
                q.add(cur.right);
            }
        }
        return root;
    }

    public static void pre(tree root, ArrayList<Integer> ans) {
        if (root == null) return;
        ans.add(root.data);
        pre(root.left, ans);
        pre(root.right, ans);
    }

    public static void inorder(tree root, ArrayList<Integer> ans) {
        if (root == null) return;
        inorder(root.left, ans);
        ans.add(root.data);
        inorder(root.right, ans);
    }

    public static void post(tree root, ArrayList<Integer> ans) {
        if (root == null) return;
        post(root.left, ans);
        post(root.right, ans);
        ans.add(root.data);
    }

    public static void iterativeinorder(tree root) {
        ArrayList<Integer> ans = new ArrayList<>();
        Stack<tree> st = new Stack<>();

        while (true) {
            if (root != null) {
                st.push(root);
                root = root.left;
            } else {
                if (st.isEmpty()) break;
                root = st.pop();
                ans.add(root.data);
                root = root.right;
            }
        }
        System.out.println("Iterative Inorder:");
        for (int ch : ans) {
            System.out.print(ch + " ");
        }
        System.out.println();
    }

    public static void iterativepre(tree root) {
        ArrayList<Integer> ans = new ArrayList<>();
        Stack<tree> st = new Stack<>();

        if (root != null) st.push(root);

        while (!st.isEmpty()) {
            tree n = st.pop();
            ans.add(n.data);
            if (n.right != null) st.push(n.right);
            if (n.left != null) st.push(n.left);
        }
        System.out.println("Iterative Preorder:");
        for (int ch : ans) {
            System.out.print(ch + " ");
        }
        System.out.println();
    }

    public static void inprepost(tree root) {
        ArrayList<Integer> in = new ArrayList<>();
        ArrayList<Integer> pre = new ArrayList<>();
        ArrayList<Integer> post = new ArrayList<>();
        Stack<Pair<tree, Integer>> st = new Stack<>();
        st.push(new Pair<>(root, 1));

        while (!st.isEmpty()) {
            Pair<tree, Integer> cur = st.pop();
            if (cur.getValue() == 1) {
                pre.add(cur.getKey().data);
                cur = new Pair<>(cur.getKey(), 2);
                st.push(cur);
                if (cur.getKey().left != null) {
                    st.push(new Pair<>(cur.getKey().left, 1));
                }
            } else if (cur.getValue() == 2) {
                in.add(cur.getKey().data);
                cur = new Pair<>(cur.getKey(), 3);
                st.push(cur);
                if (cur.getKey().right != null) {
                    st.push(new Pair<>(cur.getKey().right, 1));
                }
            } else {
                post.add(cur.getKey().data);
            }
        }

        System.out.println("Preorder: " + pre);
        System.out.println("Inorder: " + in);
        System.out.println("Postorder: " + post);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, -1, -1, 5};
        tree root = levelorder(arr);

        // Recursive traversals
        ArrayList<Integer> ans = new ArrayList<>();
        pre(root, ans);
        System.out.println("Preorder: " + ans);

        ans.clear();
        inorder(root, ans);
        System.out.println("Inorder: " + ans);

        ans.clear();
        post(root, ans);
        System.out.println("Postorder: " + ans);

        // Iterative traversals
        iterativeinorder(root);
        iterativepre(root);

        // Combined in-pre-post traversal
        inprepost(root);
    }
}
