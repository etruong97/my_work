/*
C343 / Summer 2019
Homework 01
Evan Truong
etruong
 */

import java.util.Random;
import static java.lang.System.out;

public class RandomChunkOfDNA {

    // generate a random DNA sequence of length n:
    public String nextDNA(int n) {
        String lDNA = "";
        Random lRandomizer = new Random();

        for (int i = 0; i < n; i++) {
            int j = lRandomizer.nextInt(4);
            if (j == 0) lDNA += "A";
            else if (j == 1) lDNA += "T";
            else if (j == 2) lDNA += "C";
            else if (j == 3) lDNA += "G";
        }
        return lDNA;
    }

    public String[] DNAPair(int n) {
        String[] pair = new String[2];
        pair[0] = nextDNA(n);
        pair[1] = nextDNA(n);
        return pair;
    }

    public static void main(String[] argv) {
        RandomChunkOfDNA rndDNAGenerator = new RandomChunkOfDNA();
        String dna;
        for (int i = 10; i<=1000; i = i * 10) {
            out.println("");
            dna = rndDNAGenerator.nextDNA(i);
            out.println("a DNA sequence " + i + " characters long: " + dna);
        }

        System.out.println();
        String[] p1 = rndDNAGenerator.DNAPair(100);
        System.out.println(p1[0]);
        System.out.println(p1[1]);
    }
}
