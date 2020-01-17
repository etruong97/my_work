/*
C343 Summer 2019
HW04
Evan Truong
etruong
 */

import java.util.Observable;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class HW04Model extends Observable {
    private int[][] dMatrix;
    private char[][] eMatrix;

    public HW04Model () {

    }

    public int[][] getDMatrix() {return this.dMatrix;}

    public char[][] getEMatrix() {return this.eMatrix;}

    public String fileToString (String s) {
        String str = "";
        try {
            File inFile = new File(s);
            Scanner inScan = new Scanner(inFile);
            while(inScan.hasNextLine()) {
                String line = inScan.nextLine();
                str = str + line;
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return str;
    }

    public int dist(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();
        dMatrix = new int[n + 1][m + 1];
        eMatrix = new char[n + 1][m + 1];

        if(n == 0) {
            return m;
        }

        if(m == 0) {
            return n;
        }

        int[][] matrix = new int[n+1][m+1];

        for(int i = 0; i < n+1; i++) {
            matrix[i][0] = i;
        }

        for(int j = 0; j < m+1; j++) {
            matrix[0][j] = j;
        }

        int cost;

        for(int a = 1; a < n+1; a++) {
            char c1 = s1.charAt(a-1);
            for(int b = 1; b < m+1; b++) {
                char c2 = s2.charAt(b-1);

                if(c1 == c2) {
                    cost = 0;
                }
                else {
                    cost = 1;
                }

                int subCost = matrix[a-1][b-1] + cost;
                int delCost = matrix[a][b-1] + 1;
                int insCost = matrix[a-1][b] + 1;

                int min = Math.min(subCost, Math.min(delCost, insCost));

                matrix[a][b] = min;

                if (min == delCost) {
                    eMatrix[a][b] = 'D';
                } else if (min == insCost) {
                    eMatrix[a][b] = 'I';
                } else {
                    if (cost == 0) {
                        eMatrix[a][b] = ' ';
                    } else {
                        eMatrix[a][b] = 'S';
                    }
                }

                dMatrix = matrix;
            }
            setChanged();
            notifyObservers();
        }
        this.dMatrix = matrix;
        return matrix[n-1][m-1];
    }

    public int[] dLine(int n) {
        return this.dMatrix[n];
    }

    public char[] eLine(int n) {
        return this.eMatrix[n];
    }

    public String aString() {
        return fileToString("flatland1.txt");
    }

    public String bString() {
        return fileToString("flatland2.txt");
    }

    public static void main(String[] args) {
        HW04Model model = new HW04Model();
        System.out.println(model.dist(model.fileToString("flatland1.txt"), model.fileToString("flatland2.txt")));
        for(char i : model.eLine(100)) {
            System.out.print(i + " ");
        }
    }
}
