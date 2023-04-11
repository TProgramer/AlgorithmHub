import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++) {
			
			int N = sc.nextInt(), M = sc.nextInt();
			dp = new int[M + 1][N + 1];
			System.out.println(combination(M, N));
		}
	}
	
	public static int combination(int n, int r) {
		
		if(dp[n][r] != 0) return dp[n][r];
		if(n == r || r == 0) return 1;
		return dp[n][r] = combination(n - 1, r - 1) + combination(n - 1, r);
	}

	static int dp[][];
}
