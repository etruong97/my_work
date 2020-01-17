/*
C343 Summer 2019
HW03
Evan Truong
etruong
 */

public interface Int2DArrayADT {
    void set(int r, int c, int n);

    int get(int r, int c);

    void zeroArray();

    int[] getRow(int r);

    int[] getCol(int c);

    void setRow(int[] arr, int r);

    void setCol(int[] arr, int c);

}
