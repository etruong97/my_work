/*
C343 / Summer 2019
Lab 07
Evan Truong
etruong
 */

public class RemoveAt {

    public static int removeAtStatic(Integer index, Integer[] arr) {
        int x = arr[index];
        arr[index] = null;
        return x;
    }

    public static void main(String[] args) {
        Integer[] a1 = new Integer[] {1,2,3,4,5,6};
        Integer x = removeAtStatic(2, a1);
        System.out.println(x);
        System.out.println();

        for(Integer i : a1) {
            System.out.println(i);
        }
    }
}

