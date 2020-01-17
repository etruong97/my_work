/*
C343 / Summer 2019
Lab 07
Evan Truong
etruong
 */

public class RemoveAtDynamic {
    private int[] array;

    public RemoveAtDynamic(int[] arr) {
        this.array = arr;
    }

    public int removeAtDynamic(int index) {
        int x = this.array[index];
        int[] newArray = new int[this.array.length - 1];

        for(int i = index; i < this.array.length - 1; i++) {
            this.array[i] = this.array[i + 1];
        }

        for(int j = 0; j < this.array.length -1; j++) {
            newArray[j] = this.array[j];
        }

        this.array = newArray;

        return x;
    }

    public static void main(String[] args) {
        int[] a1 = new int[] {1,2,3,4,5,6};
        RemoveAtDynamic r = new RemoveAtDynamic(a1);
        System.out.println(r.removeAtDynamic(2));
        System.out.println();

        for(int i : r.array) {
            System.out.println(i);
        }
    }
}
