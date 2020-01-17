/*
C343 Summer 2019
HW03
Evan Truong
etruong
 */

public class Int2DArray implements Int2DArrayADT {
    private int row;
    private int col;
    private int[][] array;

    public Int2DArray(int row, int col) {
        this.row = row;
        this.col = col;
        this.array = new int[row][col];
    }

    public void set(int r, int c, int n) {
        this.array[r][c] = n;
    }

    public int get(int r, int c) {
        return this.array[r][c];
    }

    public void zeroArray() {
        for (int i = 0; i < this.row; i++) {
            for (int j = 0; j < this.col; j++) {
                this.array[i][j] = 0;
            }
        }
    }

    public int[] getRow(int r) {
        int[] arr = new int[this.col];
        for (int i = 0; i < this.col; i++) {
            arr[i] = this.array[r][i];
        }
        return arr;
    }

    public int[] getCol(int c) {
        int[] arr = new int[this.row];
        for (int i = 0; i < this.row; i++) {
            arr[i] = this.array[i][c];
        }
        return arr;
    }

    public String toString() {
        String str = "";

        for (int i = 0; i < this.row; i++) {
            for (int j = 0; j < this.col; j++) {
                str = str + this.get(i, j);

                if (j == this.col - 1) {
                    if (i != this.row - 1) {
                        str = str + "\n";
                    }
                } else {
                    str = str + ", ";
                }
            }
        }
        str = str + "\n";

        return str;
    }

    public static String listToString(int[] ls) {
        String str = "[";
        for (int i = 0; i < ls.length; i++) {
            if (i == ls.length - 1) {
                str = str + ls[i] + "]";
            } else {
                str = str + ls[i] + ", ";
            }

        }

        return str;
    }

    public void setRow(int[] arr, int r) {
        for (int i = 0; i < arr.length; i++) {
            this.array[r][i] = arr[i];
        }
    }

    public void setCol(int[] arr, int c) {
        for (int i = 0; i < arr.length; i++) {
            this.array[i][c] = arr[i];
        }
    }
}
