import java.lang.Comparable;

public class Binary <K extends Comparable<?super K>> {

    public Binary() {}

    public int search(K[] arr, int low, int high, K val) {
        if(low < high) {
            int mid = (low + high) / 2;

            if(val.compareTo(arr[mid]) == 0) {
                return mid;
            }
            else if(val.compareTo(arr[mid]) > 0)
            {
                return search(arr, mid + 1, high, val);
            }
            else {
                return search(arr, low, mid, val);
            }
        }
        else {
            return arr.length;
        }
    }

    public static void main(String[] args) {
        Binary s = new Binary();

        Integer[] a1 = new Integer[] {3,5,6,7,10,12,15,17,18};
        String[] a2 = new String[] {"a", "b", "e", "h", "k", "z"};
        Double[] a3 = new Double[] {0.1, 1.0, 2.32, 9.0, 13.14};

        // should be found
        System.out.println(s.search(a1, 0, a1.length,7));
        // should not be found
        System.out.println(s.search(a1, 0, a1.length,120));
        // should be found
        System.out.println(s.search(a2, 0, a2.length,"e"));
        // should not be found
        System.out.println(s.search(a2, 0, a2.length,"y"));
        // should be found
        System.out.println(s.search(a3, 0, a3.length,9.0));
        // should not be found
        System.out.println(s.search(a3, 0, a3.length,10.0));
    }
}
