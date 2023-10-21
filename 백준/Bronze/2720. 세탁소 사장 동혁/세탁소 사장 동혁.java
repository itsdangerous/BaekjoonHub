import java.util.*;
import java.io.*;
public class Main {

    static int T;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for( int tc=0; tc < T; tc ++) {
            int C = Integer.parseInt(br.readLine());
            int[] result = solve(C);
            printArr(result);
        }

    }

    static int[] solve(int c) {
        int[] result = new int [4];
        result[0] = c / 25;
        c = c % 25;
        result[1] = c / 10;
        c = c% 10;
        result[2] = c / 5;
        c = c % 5;
        result[3] = c;

        return result;
    }
    static void printArr(int[] arr) {
        for(int i=0; i<arr.length; i++) {
            System.out.print(arr[i]+ " ");
        }
        System.out.println();
    }
}