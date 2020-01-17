/*
C343 / Summer 2019
Homework 01
Evan Truong
etruong
 */

public class HammingDNADistance {

    public static int distance(String s1, String s2) {
        int count = 0;

        for(int i = 0; i < s1.length(); i++) {
            if(s1.charAt(i) != s2.charAt(i)) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        RandomChunkOfDNA rand = new RandomChunkOfDNA();
        String[] dna1 = rand.DNAPair(100);
        String[] dna2 = rand.DNAPair(100);
        String[] dna3 = rand.DNAPair(100);

        System.out.println(dna1[0]);
        System.out.println(dna1[1]);
        System.out.println(distance(dna1[0], dna1[1]));
        System.out.println();
        System.out.println(dna2[0]);
        System.out.println(dna2[1]);
        System.out.println(distance(dna2[0], dna2[1]));
        System.out.println();
        System.out.println(dna3[0]);
        System.out.println(dna3[1]);
        System.out.println(distance(dna3[0], dna3[1]));
    }
}