public class MinHeap <Key extends Comparable<? super Key>, E> {
	/** store the elements in an array, listArray */
	private BinNode<Key, E>[] listArray;
	private int listSize;
	private int maxSize;
	public MinHeap(int maxn, int num, BinNode<Key, E>[] inp) { 
		maxSize = maxn;
		listSize = num;
		listArray = inp;
		heapify(); 
	}
	public void heapify() {
		/** note siftDown is applied from the middle node to the start 
		 * so the children of a node are visited before the node itself 
		 * (subtrees are already heaps)
		 */
		for(int i = listSize/2 - 1; i >= 0; i --) {
			siftDown(i);
		}
	}
	public int length() { return listSize; }
	public void insert(BinNode<Key, E> inp) {
		assert listSize < maxSize : "exceed maxSize " + maxSize;
		listArray[listSize ++] = inp;
		/** sift up the newly added node if it is less than its ancestors */
		siftUp(listSize - 1); 
	}
	public BinNode<Key, E> removeMin() {
		return remove(0);
	}
	public BinNode<Key, E> remove(int pos) {
		assert (pos >= 0) && (pos < listSize) : "Illegal remove";
		if(pos == listSize -1) listSize --;
		else {
			/** swap the max (at position 0) with the last one, then remove the last one */
			swapNodes(pos, --listSize);
			/** call siftUp() & siftDown() to restore the heap */
			if(pos > 0) siftUp(pos);
			if(!isLeaf(pos)) siftDown(pos);
		}
		return listArray[listSize];
	}
	public void siftDown(int pos) {
		assert (pos >= 0) && (pos < listSize) : "Illegal heap position";
		/** System.out.println("now work on " + pos); */
		while(!isLeaf(pos)) {
			int i = left(pos);
			/** if the right child is less than the left child, use the right child */
			if((i < listSize - 1) && (((Key) listArray[i].getKey()).compareTo((Key) listArray[i + 1].getKey()) > 0)) i ++;
			if(((Key) listArray[i].getKey()).compareTo((Key) listArray[pos].getKey()) < 0) {
				swapNodes(i, pos);
			}
			else break;
			pos = i;
		}
	}
	public void siftUp(int pos) {
		while(pos > 0) {
			int p = parent(pos);
			if(((Key) listArray[pos].getKey()).compareTo((Key)listArray[p].getKey()) < 0) {
				swapNodes(p, pos);
			}
			else break;
			pos = p;
		}
	}
	public void swapNodes(int i, int j) {
		BinNode<Key, E> tmp = listArray[i];
		listArray[i] = listArray[j];
		listArray[j] = tmp;
	}
	public boolean isLeaf(int pos) {
		if(pos < listSize/2) return false;
		else return true;
	}
	public int left(int pos) { 
		assert 2 * pos + 1 < listSize : "left child is empty";
		return 2 * pos + 1; 
	}
	public int right(int pos) { 
		assert 2 * pos + 2 < listSize : "right child is empty";
		return 2 * pos + 2; 
	}
	public int parent(int pos) {
		assert pos > 0 : "the node is already a root"; 
		return (int) Math.floor((pos - 1) / 2);
	}
	public void display() {
		String output = "[HeapSize: " + listSize + "] ";
		for(int i = 0; i < listSize; i ++) output += " " + listArray[i].getKey() + "(" + listArray[i].getValue() + ")";
		System.out.println(output);
	}
}
