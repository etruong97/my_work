public class BinNode <K extends Comparable<?super K>> {
    private K key;             // only key, no value
    private BinNode<K> left;   // left child
    private BinNode<K> right;  // right child

    private int size;          // the size (number of nodes)
    // of the subtree rooted at this node

    public BinNode(K k) {
        key = k;
        left = right = null;
        size = 1;
    }

    public void setLeft(BinNode<K> node) {
        left = node;
    }

    public void setRight(BinNode<K> node) {
        right = node;
    }

    public boolean isLeaf() {
        if (left == null && right == null)
            return true;
        else
            return false;
    }

    public BinNode<K> getLeft() {
        return left;
    }

    public BinNode<K> getRight() {
        return right;
    }

    public K getKey() {
        return key;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int newsize) {
        size = newsize;
    }
}
