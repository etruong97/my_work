import java.util.Random;
import java.util.Observable;

public class Lab12Model extends Observable {
    private int[] array;

    public Lab12Model(int n) {
        Random r = new Random();

        this.array = new int[n];
        for(int i = 0; i < n; i++) {
            this.array[i] = r.nextInt(500);
        }
    }

    public int[] getArray() {
        return this.array;
    }

    public void sort() {
        int n = this.array.length;

        for (int i = 1; i < n; ++i) {
            int key = this.array[i];
            int j = i - 1;

            while (j >= 0 && this.array[j] > key) {
                this.array[j + 1] = this.array[j];
                j = j - 1;
                setChanged();
                notifyObservers();
            }
            array[j + 1] = key;

        }
    }

    public static void main(String[] args) {
        Lab12Model model = new Lab12Model(10);

        for(int i : model.array) {
            System.out.print(i + " ");
        }

        model.sort();
        System.out.println();

        for(int x : model.array) {
            System.out.print(x + " ");
        }
    }
}
