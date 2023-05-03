import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int score = 0;
	static int[][] cols = {{0}, {0, 1}, {0}};
	
	static void removeRow(int[][] board, int row) {
		for (int i = row; i > 0; i--) {
			for (int j = 0; j < 4; j++) {
				board[i][j] = board[i-1][j];
			}
		}
		
		Arrays.fill(board[0], 0);
	}
	
	static int getMaximumRow(int[][] board, int col) {
		for (int i = 0; i < 4; i++) {
			if (board[i][col] != 0) {
				return (i - 1);
			}
		}
		
		return 3;
	}
	
	static void moveBlock(int[][] board, int x, int y) {
		board[x][y] = 1;
	}
	
	static boolean checkRow(int[][] board, int row) {
		for (int col = 0; col < 4; col++) {
			if (board[row][col] == 0) {
				return false;
			}
		}
		
		return true;
	}
	
	static void process(int[][] board, int t, int x, int y) {
		//System.out.println();
		//System.out.println();
		//System.out.println("t:" + t);
		//System.out.println("x:" + x);
		//System.out.println("y:" + y);
		//System.out.println("before:");
		//print(board);
		
		int minimumRow = 3;
		for (int col : cols[t-1]) {
			minimumRow = Math.min(getMaximumRow(board, col + y), minimumRow);
		}

		if (minimumRow < 0) {
			removeRow(board, 3);
			minimumRow = 0;
		}
		
		//System.out.println("minimumRow:" + minimumRow);
		//print(board);
		
		moveBlock(board, minimumRow, y);
		if (t == 2) {
			moveBlock(board, minimumRow, y + 1);
		}
		
		//System.out.println("after:");
		//print(board);
		
		if (checkRow(board, minimumRow)) {
			score++;
			removeRow(board, minimumRow);
		}
		
		//System.out.println("check:");
		//print(board);
	}
	
	static int countBlock(int[][] board) {
		int count = 0;
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (board[i][j] > 0) {
					count++;
				}
			}
		}
		
		return count;
	}
	
	static void print(int[][] board) {
		System.out.println();
		for (int i = 0; i < 4; i++) {
			System.out.println(Arrays.toString(board[i]));
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int[][] green = new int[4][4];
		int[][] blue = new int[4][4];
		
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			
			int t = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			process(green, t, x, y);
			
			if (t == 1) {
				process(blue, 1, y, x);
			}
			if (t == 2) {
				process(blue, 3, y, x);
				process(blue, 3, y, x);
			}
			if (t == 3) {
				process(green, t, x, y);
				process(blue, 2, y, x);
			}
		}
		
		System.out.println(score);
		System.out.println(countBlock(blue) + countBlock(green));
		
		br.close();
	}

}