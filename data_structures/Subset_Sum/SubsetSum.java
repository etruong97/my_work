import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class SubsetSum {

    public SubsetSum() {}

    public boolean recursiveSubsetSum(int[] arr, int k) {
        int n = arr.length;
        return recursiveSubsetSum(arr, k, n);
    }

    public boolean recursiveSubsetSum(int[] arr, int k, int n) {
        if(k == 0) {
            return true;
        }
        if(k != 0 && n == 0) {
            return false;
        }

        return recursiveSubsetSum(arr, k, n - 1) ||
                recursiveSubsetSum(arr, k - arr[n-1], n - 1);
    }

    public boolean subsetSumDP(int[] arr, int k) {
        int n = arr.length;
        boolean[][] matrix = new boolean[k + 1][n];

        for(int i = 0; i < n; i++) {
            matrix[0][i] = true;
        }

        for(int i = 1; i < k + 1; i++) {
            for(int j = 0; j < n; j++) {
                if(i - arr[j] == 0) {
                    matrix[i][j] = true;
                }
                else if(i - arr[j] < 0) {
                    matrix[i][j] = false;
                }
                else if(j - 1 < 0) {
                    matrix[i][j] = false;
                }
                else {
                    matrix[i][j] = matrix[i - arr[j]][j - 1];
                }
                if(matrix[i][j]) {
                    for(int a = j + 1; a < n; a++) {
                        matrix[i][a] = true;
                    }
                    break;
                }
            }
        }
        return matrix[k][n -1];
    }

    public static void main(String[] args) {
        SubsetSum s = new SubsetSum();

        int[] arr = new int[] {2,20,5,8,11,12,4,10,21,19};
        System.out.println(s.recursiveSubsetSum(arr,0));
        System.out.println(s.recursiveSubsetSum(arr,25));
        System.out.println(s.recursiveSubsetSum(arr,1));
        System.out.println(s.recursiveSubsetSum(arr,1100));
        System.out.println(s.recursiveSubsetSum(arr,100));
        System.out.println(s.recursiveSubsetSum(arr,250));
        System.out.println();
        System.out.println(s.subsetSumDP(arr,0));
        System.out.println(s.subsetSumDP(arr,25));
        System.out.println(s.subsetSumDP(arr,1));
        System.out.println(s.subsetSumDP(arr,1100));
        System.out.println(s.subsetSumDP(arr,100));
        System.out.println(s.subsetSumDP(arr,250));
        System.out.println();

        int[] arr2 = new int[] {1,2,3,10,9,8,20,21,22,23};
        System.out.println(s.recursiveSubsetSum(arr2,0));
        System.out.println(s.recursiveSubsetSum(arr2,6));
        System.out.println(s.recursiveSubsetSum(arr2,1000));
        System.out.println(s.recursiveSubsetSum(arr2,66));
        System.out.println(s.recursiveSubsetSum(arr2,99));
        System.out.println();
        System.out.println(s.subsetSumDP(arr2,0));
        System.out.println(s.subsetSumDP(arr2,6));
        System.out.println(s.subsetSumDP(arr2,1000));
        System.out.println(s.subsetSumDP(arr2,66));
        System.out.println(s.subsetSumDP(arr2,99));
        System.out.println();

        int[] arr3 = new int[] {100,10,1000,1,5,50,500,10000,6,7};
        System.out.println(s.recursiveSubsetSum(arr3,0));
        System.out.println(s.recursiveSubsetSum(arr3,110));
        System.out.println(s.recursiveSubsetSum(arr3,1006));
        System.out.println(s.recursiveSubsetSum(arr3,70));
        System.out.println(s.recursiveSubsetSum(arr3,551));
        System.out.println();
        System.out.println(s.subsetSumDP(arr3,0));
        System.out.println(s.subsetSumDP(arr3,110));
        System.out.println(s.subsetSumDP(arr3,1006));
        System.out.println(s.subsetSumDP(arr3,70));
        System.out.println(s.subsetSumDP(arr3,551));


    }
}
