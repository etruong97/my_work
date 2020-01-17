public class BSTJr <K extends Comparable<?super K>> {
    BinNode<K> root;
    BinNode<K> curr;

    // TODO for C343/Summer 2019 - Lab 09
    // "unbalanced" is used for balance checking:
    //    if a node is unbalanced, the tree will be unbalanced
    BinNode<K> unbalanced = null;

    public BSTJr() {
        root = null;
        curr = null;
    }
    public void build(K[] ks) {
        for (int i = 0; i < ks.length; i ++)
            insert(ks[i]);
    }
    public void insert(K k) {
        BinNode<K> t = new BinNode<K>(k);
        if (root == null) {
            root = curr = t;
        } else {
            curr = search(root, k);
            if (k.compareTo(curr.getKey()) < 0)
                curr.setLeft(t);
            else
                curr.setRight(t);
        }
    }
    public BinNode<K> search(BinNode<K> entry, K k) {
        if (entry == null)
            return null;
        else {
            entry.setSize(entry.getSize() + 1); //update the size of the subtree by one
            if (entry.isLeaf())
                return entry;
            if (k.compareTo(curr.getKey()) < 0) {
                if (entry.getLeft() != null)
                    return search(entry.getLeft(), k);
                else
                    return entry;
            } else {
                if (entry.getRight() != null)
                    return search(entry.getRight(), k);
                else
                    return entry;
            }
        }
    }
    public void display() {
        if(root == null) return;
        System.out.println("Preorder enumeration: key(size-of-the-subtree)");
        preorder(root);
        System.out.println();
    }
    public void preorder(BinNode<K> entry) {
        System.out.print(entry.getKey() + "(" + entry.getSize() + ") ");
        if(entry.getLeft() != null) preorder(entry.getLeft());
        if(entry.getRight() != null) preorder(entry.getRight());
    }

    public void inorder(BinNode<K> entry) {
        if(entry.getLeft() != null) inorder(entry.getLeft());
        System.out.print(entry.getKey() + "(" + entry.getSize() + ") ");
        if(entry.getRight() != null) inorder(entry.getRight());
    }

    public void postorder(BinNode<K> entry) {
        if(entry.getLeft() != null) postorder(entry.getLeft());
        if(entry.getRight() != null) postorder(entry.getRight());
        System.out.print(entry.getKey() + "(" + entry.getSize() + ") ");
    }

    public int height() {
        return height(this.root);
    }

    public int height(BinNode b) {
        int sum = 0;
        if(b == null) {
            return sum;
        }
        else {
            return Math.max(height(b.getLeft()), height(b.getRight())) + 1;
        }
    }

    public boolean checkBalance() {
        return checkBalance(this.root);
    }

    public boolean checkBalance(BinNode b) {
        if(b == null) {
            return true;
        }
        else {
            int diff = Math.abs(height(b.getLeft()) - height(b.getRight()));
            return checkBalance(b.getLeft()) && checkBalance(b.getRight()) && diff <= 1;
        }
    }

    // TODO for C343/Summer 2019 - Lab 09
    // implement checkBalance(), perhaps write treeHeight(node) as helper function

    public static void main(String[] argv) {
        BSTJr tree = new BSTJr();

        BinNode<Integer> root = new BinNode<Integer>(20);
        BinNode<Integer> node1 = new BinNode<Integer>(10);
        BinNode<Integer> node2 = new BinNode<Integer>(40);
        root.setLeft(node1);
        root.setRight(node2);
        BinNode<Integer> node3 = new BinNode<Integer>(5);
        node1.setLeft(node3);
        BinNode<Integer> node4 = new BinNode<Integer>(15);
        node1.setRight(node4);
        BinNode<Integer> node5 = new BinNode<Integer>(30);
        node2.setLeft(node5);
        BinNode<Integer> node6 = new BinNode<Integer>(100);
        node2.setRight(node6);
        System.out.println(tree.checkBalance(root));
        BinNode<Integer> node7 = new BinNode<Integer>(4);
        BinNode<Integer> node8 = new BinNode<Integer>(3);
        node3.setLeft(node7);
        node7.setLeft(node8);
        System.out.println(tree.checkBalance(root));
    }
}
