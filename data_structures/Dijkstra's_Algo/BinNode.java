public class BinNode<Key, E> {
    private Key key;
    private E value;
    private BinNode<Key, E> left;
    private BinNode<Key, E> right;
    public BinNode(Key k, E e) {
        key = k;
        value = e;
        left = right = null;
    }
    public Key getKey() { return key; }
    public E getValue() { return value; }
    public void setKey(Key k) { key = k; }
    public void setValue(E e) { value = e; }
    public void setLeft(BinNode<Key, E> node) { left = node; }
    public void setRight(BinNode<Key, E> node) { right = node; }
    public void removeLeft() { left = null; }
    public void removeRight() { right = null; }
    public BinNode<Key, E> getLeft() { return left; }
    public BinNode<Key, E> getRight() { return right; }
    public boolean isLeaf() {
        if((left == null) && (right == null)) return true;
        else return false;
    }
    public String inorder() {
        String tmp = "";
        if (left != null) {
            tmp = tmp + left.inorder();
        }
        tmp = tmp + "["+ key + ":" + value + "]";
        if (right != null) {
            tmp = tmp + right.inorder();
        }
        return tmp;
    }
}
