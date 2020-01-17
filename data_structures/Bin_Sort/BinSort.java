import java.lang.reflect.Array;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Random;

public class BinSort {

    public BinSort() {}

    public int[] binSort(int[] arr) {
        ArrayList<LinkedList<Integer>> binList = new ArrayList<>();
        int max = this.maximum(arr);

        for(int i = 0; i <= max; i++) {
            LinkedList<Integer> node = new LinkedList<>();
            binList.add(node);
        }

        for(int i : arr) {
            binList.get(i).addLast(i);
        }

        int[] finalArr = new int[arr.length];

        int pos = 0;

        for(LinkedList<Integer> ls : binList) {
            for(int n : ls) {
                finalArr[pos] = n;
                pos++;
            }
        }

        return finalArr;
    }

    public int maximum(int[] arr) {
        int max = 0;

        for(int i : arr) {
            if(i > max) {
                max = i;
            }
        }

        return max;
    }

    public static void main(String[] args) {
        Random r = new Random();

        BinSort b = new BinSort();
        int[] a1 = new int[] {5,4,3,2,1,6,7,0,10};

        for(int i : b.binSort(a1)) {
            System.out.print(i + " ");
        }

        System.out.println();

        int[] a2 = new int[25];
        for(int i = 0; i < a2.length; i++) {
            a2[i] = r.nextInt(100);
        }

        for(int i : b.binSort(a2)) {
            System.out.print(i + " ");
        }
    }
}
