import java.io.*;
import java.util.*;

public class Main {

    static final int THRESHOLD = 15;
    static int N = 5;
    static char[][] alpha = new char[N][THRESHOLD];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        initArr();

        for (int i =0; i< N; i ++) {
            char[] charArr = br.readLine().toCharArray();
            for (int j = 0; j < charArr.length; j++) {
                alpha[i][j] = charArr[j];
            }
        }

        solve();

    }
    static void solve() {
        for (int c=0; c<THRESHOLD; c++) {
            for (int r=0; r<N; r++) {
                if (alpha[r][c] == '-') continue;
                System.out.print(alpha[r][c]);
            }
        }
    }
    static void initArr() {
        for (int i=0; i<N; i++ ) {
            Arrays.fill(alpha[i], '-');
        }
    }

}