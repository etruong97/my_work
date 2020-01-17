public class BinNodeJr <E extends Comparable<?super E>>{
    private E value;
    private BinNodeJr<E> left;
    private BinNodeJr<E> right;

    public BinNodeJr(E e) {
        value = e;
        left = right = null;
    }

    public void setLeft(BinNodeJr<E> node) {
        left = node;
    }

    public void setRight(BinNodeJr<E> node) {
        right = node;
    }

    public boolean find(E q) {
        if(this.value == q) {
            return true;
        }
        else if (this.left == null && this.right == null) {
            return false;
        }
        else if(this.left == null && this.right != null) {
            return this.right.find(q);
        }
        else if(this.left != null && this.right == null) {
            return this.left.find(q);
        }
        else {
            return this.left.find(q) || this.right.find(q);
        }
    }

    public static void main(String[] argv) {
        BinNodeJr<Integer> root = new BinNodeJr<Integer>(9);
        BinNodeJr<Integer> node1 = new BinNodeJr<Integer>(29);
        BinNodeJr<Integer> node2 = new BinNodeJr<Integer>(39);
        root.setLeft(node1);
        root.setRight(node2);
        BinNodeJr<Integer> node3 = new BinNodeJr<Integer>(49);
        node1.setLeft(node3);
        BinNodeJr<Integer> node4 = new BinNodeJr<Integer>(20);
        node1.setRight(node4);
        BinNodeJr<Integer> node5 = new BinNodeJr<Integer>(11);
        node2.setLeft(node5);
        BinNodeJr<Integer> node6 = new BinNodeJr<Integer>(80);
        node2.setRight(node6);
        BinNodeJr<Integer> node7 = new BinNodeJr<Integer>(50);
        node3.setLeft(node7);
        BinNodeJr<Integer> node8 = new BinNodeJr<Integer>(41);
        node3.setRight(node8);
        BinNodeJr<Integer> node9 = new BinNodeJr<Integer>(32);
        node4.setLeft(node9);

        // find() needs to be implemented
        System.out.println("39 is found in the tree: " + root.find(39));
        // find(39) shall return true
        System.out.println("100 is found in the tree: " + root.find(100));
        // find(100) shall return false
        System.out.println("50 is found in the tree: " + root.find(50));
    }
}
