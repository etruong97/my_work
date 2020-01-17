/*
C343 Summer 2019
HW03
Evan Truong
etruong
 */

import java.util.Random;
import java.util.Observable;

public class HW03Model extends Observable {
    private Int2DArray array;
    private int height;
    private int width;

    public HW03Model(int h, int w) {
        this.height = h;
        this.width = w;
        this.array = new Int2DArray(h,w);
    }

    public Int2DArray getArray() {
        return this.array;
    }

    public int getHeight() {
        return this.height;
    }

    public int getWidth() {
        return this.width;
    }

    public void randomize() {
        System.out.println("Randomizing");
        Random r = new Random(1);

        for(int i = 0; i < this.height; i++) {
            for(int j = 0; j < this.width; j++) {
                int value = r.nextInt(255 + 255 + 1) - 255;

                this.array.set(i, j, value);
            }
        }
        setChanged();
        notifyObservers();
    }

    public static void sort(int[] arr) {
    int n = arr.length;

    for (int i = 1; i < n; ++i) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

    private void sortColumn() {
        for(int i = 0; i < this.width; i++) {
            int[] col = new int[this.height];
            for(int j = 0; j < this.height; j++) {
                col[j] = this.array.get(j,i);
            }
            sort(col);
            this.array.setCol(col,i);
        }
    }

    private void sortRow() {
        for(int i = 0; i < this.height; i++) {
            int[] row = new int[this.width];
            for(int j = 0; j < this.width; j++) {
                row[j] = this.array.get(i,j);
            }
            sort(row);
            this.array.setRow(row,i);
        }
    }

    public void sortArray1() {
        this.sortColumn();
        this.sortRow();
        setChanged();
        notifyObservers();
    }

    public void sortArray2() {
        this.sortRow();
        this.sortColumn();
        setChanged();
        notifyObservers();
    }

    public static void main(String[] args) {
        HW03Model c1 = new HW03Model(1000,1000);
        c1.randomize();

        long timeBefore = System.nanoTime();
        c1.sortArray1();
        long timeAfter = System.nanoTime();
        long timeElapsed = timeAfter - timeBefore;

        HW03Model c2 = new HW03Model(1000,1000);
        c2.randomize();

        long timeBefore2 = System.nanoTime();
        c2.sortArray2();
        long timeAfter2 = System.nanoTime();
        long timeElapsed2 = timeAfter2 - timeBefore2;

        System.out.println("Sort 1: " + timeElapsed);
        System.out.println("Sort 2: " + timeElapsed2);
    }
}
