/*swea_1249 : 보급로
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
*/

import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {
    static int[][] map;
    static int N;
    static boolean[][] visited;
    static int min;
    static int length;
    static int[] dr = new int[]{1, 0, -1, 0};
    static int[] dc = new int[]{0, 1, 0, -1};
    static int[][] dp;
    static int[][] depth;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int TC = 1; TC < T + 1; TC++) {

            N = Integer.parseInt(br.readLine());
            map = new int[N][N];
            visited = new boolean[N][N];
            min = Integer.MAX_VALUE/100;
            length = 0;
            dp = new int[N][N];
            depth = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dp[i][j] = Integer.MAX_VALUE;
                    depth[i][j] = Integer.MAX_VALUE;
                }
            }
            for (int i = 0; i < N; i++) {
                String str = br.readLine();
                for (int j = 0; j < N; j++) {
                    map[i][j] = str.charAt(j)-'0';
                }
            }

            dfs(0, 0, 0, 0);
            visited[0][0] = true;
//            for (int i = 0; i < N; i++) {
//                for (int j = 0; j < N; j++) {
//                    System.out.print(depth[i][j]+" ");
//                }
//                System.out.println();
//            }
            System.out.printf("#%d %d\n", TC, dp[N - 1][N - 1]);
        }

    }


    static void dfs(int r, int c, int tot, int cnt) {
        if(dp[r][c] <= tot) return;

        if(r == N-1 && c ==N-1) {
            dp[r][c] = tot;
            return;
        }
        dp[r][c] = tot;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e[2]));
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (!check(nr, nc)) continue;
            if(visited[nr][nc]) continue;
            if(dp[nr][nc] <= tot+map[nr][nc]) continue;
            pq.offer(new int[]{nr, nc, map[nr][nc]});
        }
        while (!pq.isEmpty()) {
            int[] point = pq.poll();
            visited[point[0]][point[1]] = true;
            dfs(point[0], point[1], tot + point[2], cnt + 1);
            visited[point[0]][point[1]] = false;
        }

    }

    private static boolean check(int nr, int nc) {
        return 0 <= nr && nr < N && 0 <= nc && nc < N;
    }
}