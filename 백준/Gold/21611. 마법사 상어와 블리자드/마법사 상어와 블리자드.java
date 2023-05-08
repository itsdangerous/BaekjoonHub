import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 마법사 상어와 블리자드
public class Main {
    static int N, M;
    static int[][] map;
    static int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static int[] marbleCount;
    
    static void castSpells(int d, int s) {
        int r = N / 2;
        int c = N / 2;
        
        for (int i = 0; i < s; i++) {
            r += directions[d][0];
            c += directions[d][1];
                    
            map[r][c] = 0;
        }

        moveMarbles();
    }
    
    static void moveMarbles() {
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        int r = N / 2;
        int c = N / 2;
        
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i <= N / 2; i++) {
            if (i > 0 && map[r][c] == 0) {
                q.offer(new int[] {r, c});
            } else {
                if (q.size() > 0) {
                    int[] newPosition = q.poll();
                    
                    map[newPosition[0]][newPosition[1]] = map[r][c];
                    map[r][c] = 0;
                    q.offer(new int[] {r, c});
                }
            }
            
            for (int j = 0; j < 4; j++) {
                r += dr[j];
                c += dc[j];
                
                while (Math.abs(r - N / 2) <= i && Math.abs(c - N / 2) <= i) {
                    if (map[r][c] == 0) {
                        q.offer(new int[] {r, c});
                    } else {
                        if (q.size() > 0) {
                            int[] newPosition = q.poll();
                            
                            map[newPosition[0]][newPosition[1]] = map[r][c];
                            map[r][c] = 0;
                            q.offer(new int[] {r, c});
                        }
                    }
                    
                    r += dr[j];
                    c += dc[j];
                }
                
                if (j < 3) {
                    r -= dr[j];
                    c -= dc[j];
                }
            }
        }

        checkExplosiveMarbles();
    }
    
    static void checkExplosiveMarbles() {
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        int r = N / 2;
        int c = N / 2;

        boolean flag = false;
        
        Queue<int[]> q = new LinkedList<>();
        int prevMarbleNumber = 0;
        for (int i = 0; i <= N / 2; i++) {
            if (prevMarbleNumber == map[r][c]) {
                q.offer(new int[] {r, c});
            } else {
                if (q.size() < 4) {
                    q.clear();
                    prevMarbleNumber = map[r][c];
                    q.offer(new int[] {r, c});
                } else {
                    flag = true;
                    explodeMarbles(q, prevMarbleNumber);
                }
            }
            
            for (int j = 0; j < 4; j++) {
                r += dr[j];
                c += dc[j];
                
                while (Math.abs(r - N / 2) <= i && Math.abs(c - N / 2) <= i) {
                    if (prevMarbleNumber == map[r][c]) {
                        q.offer(new int[] {r, c});
                    } else {
                        if (q.size() < 4) {
                            q.clear();
                            prevMarbleNumber = map[r][c];
                            q.offer(new int[] {r, c});
                        } else {
                            flag = true;
                            explodeMarbles(q, prevMarbleNumber);
                        }
                    }
                    
                    r += dr[j];
                    c += dc[j];
                }
                
                if (j < 3) {
                    r -= dr[j];
                    c -= dc[j];
                }
            }
        }
        
        if (flag) {
            moveMarbles();
        } else {
        	makeGroup();
        }
    }
    
    static void makeGroup() {
    	int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        int r = N / 2;
        int c = N / 2;
        
        Queue<Integer> q = new LinkedList<>();
        int prevMarbleNumber = 0;
        int count = 0;
        
        for (int i = 0; i <= N / 2; i++) {
        	if (prevMarbleNumber == map[r][c]) {
    			count++;
    		} else {
    			q.offer(count);
    			q.offer(prevMarbleNumber);
    			
    			prevMarbleNumber = map[r][c];
    			count = 1;
    		}
        		
            for (int j = 0; j < 4; j++) {
                r += dr[j];
                c += dc[j];
                
                while (Math.abs(r - N / 2) <= i && Math.abs(c - N / 2) <= i) {
                	if (prevMarbleNumber == map[r][c]) {
            			count++;
            		} else {
            			q.offer(count);
            			q.offer(prevMarbleNumber);
            			
            			prevMarbleNumber = map[r][c];
            			count = 1;
            		}
                    
                    r += dr[j];
                    c += dc[j];
                }
                
                if (j < 3) {
                    r -= dr[j];
                    c -= dc[j];
                }
            }
        }

        makeMap(q);
	}
    
    static void makeMap(Queue<Integer> q) {
    	int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        int r = N / 2;
        int c = N / 2;
    	
        map[r][c] = 0;
        q.poll();
        q.poll();
        
		 for (int i = 0; i <= N / 2; i++) {
	     	if (i > 0) {
	     		if (q.isEmpty()) {
	     			map[r][c] = 0;
	     		} else {
	     			map[r][c] = q.poll();
	     		}
	     	}
	     		
	         for (int j = 0; j < 4; j++) {
	             r += dr[j];
	             c += dc[j];
	             
	             while (Math.abs(r - N / 2) <= i && Math.abs(c - N / 2) <= i) {
	            	 if (q.isEmpty()) {
	     	     			map[r][c] = 0;
	     	     	} else {
	     	     			map[r][c] = q.poll();
	     	     	}
	            	 
	                 r += dr[j];
	                 c += dc[j];
	             }
	             
	             if (j < 3) {
	                 r -= dr[j];
	                 c -= dc[j];
	             }
	         }
	     }
    }

	static void explodeMarbles(Queue<int[]> q, int marbleNumber) {
        marbleCount[marbleNumber] += q.size();
        
        while (!q.isEmpty()) {
            int[] node = q.poll();
            map[node[0]][node[1]] = 0;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        marbleCount = new int[4];
        
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            } 
        }
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            int d = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken());
            
            castSpells(d, s);
        }
        
        int answer = 0;
        for (int i = 1; i <= 3; i++) {
            answer += marbleCount[i] * i;
        }
        
        System.out.println(answer);
        br.close();
    }
}