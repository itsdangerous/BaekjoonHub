import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int N, K;
    static int[] sensor;
    static Integer[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());

        sensor = new int[N];
        dist = new Integer[N-1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sensor[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(sensor);

        for (int i = 0; i < sensor.length - 1; i++) {
            dist[i] = sensor[i+1] - sensor[i];
        }

        Arrays.sort(dist, Collections.reverseOrder());

        int hap = 0;
        for (int i = K-1; i < N - 1; i++) {
            hap += dist[i];
        }
        System.out.println(hap);
    }

}