import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static boolean isSame(int N, int[] cur, int[] target) {
		for (int i = 0; i < N; i++) {
			if (cur[i] != target[i])
				return false;
		}
		
		return true;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] originStatus = new int[N];
		int[] targetStatus = new int[N];
		
		char[] inputOriginStatus = br.readLine().toCharArray();
		char[] inputTargetStatus = br.readLine().toCharArray();
		for (int i = 0; i < N; i++) {
			originStatus[i] = inputOriginStatus[i] - '0';
			targetStatus[i] = inputTargetStatus[i] - '0';
		}
		
		int count = 0;
		int[] curStatus = Arrays.copyOf(originStatus, N);
		
		curStatus[0] = (curStatus[0] + 1) % 2;
		curStatus[1] = (curStatus[1] + 1) % 2;
		count++;
		
		for (int i = 1; i < N - 1; i++) {
			if (curStatus[i-1] != targetStatus[i-1]) {
				curStatus[i-1] = (curStatus[i-1] + 1) % 2;
				curStatus[i] = (curStatus[i] + 1) % 2;
				curStatus[i+1] = (curStatus[i+1] + 1) % 2;
				count++;
			}
		}
		if (curStatus[N-2] != targetStatus[N-2]) {
			curStatus[N-2] = (curStatus[N-2] + 1) % 2;
			curStatus[N-1] = (curStatus[N-1] + 1) % 2;
			count++;
		}
		if (!isSame(N, curStatus, targetStatus)) {
			count = -1;
		}
		
		int cnt = 0;
		curStatus = Arrays.copyOf(originStatus, N);
		for (int i = 1; i < N - 1; i++) {
			if (curStatus[i-1] != targetStatus[i-1]) {
				curStatus[i-1] = (curStatus[i-1] + 1) % 2;
				curStatus[i] = (curStatus[i] + 1) % 2;
				curStatus[i+1] = (curStatus[i+1] + 1) % 2;
				cnt++;
			}
		}
		if (curStatus[N-2] != targetStatus[N-2]) {
			curStatus[N-2] = (curStatus[N-2] + 1) % 2;
			curStatus[N-1] = (curStatus[N-1] + 1) % 2;
			cnt++;
		}
		if (!isSame(N, curStatus, targetStatus)) {
			cnt = -1;
		}
		
		if (count >= 0 && cnt >= 0) {
			System.out.println(Math.min(count, cnt));
		} else if (count == -1 && cnt == -1){
			System.out.println(-1);
		} else {
			System.out.println(Math.max(count, cnt));
		}
		
		
		br.close();
	}

}