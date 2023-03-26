import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();
		map = new int[N][M];
		boolean isVer = false, isHor = false;
		int crossVer = 0, crossHor = 0;
		int etcVer = 0, etcHor = 0;
		
		int count = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				
				map[i][j] = sc.nextInt();
				if(map[i][j] == 0) continue; 
				count++;
				if(i > 0 && map[i - 1][j] == 1) {
					
					isVer = true;
					crossVer = i + 1; etcVer = j + 1;
				}
				if(j > 0 && map[i][j - 1] == 1) {
					
					isHor = true;
					crossHor = j + 1; etcHor = i + 1;
				}
			}
		}
		
		int res = K * 2 - count;
		System.out.println(res);
		
		if(res == 0) return;
		if(K == 1 && count == 1) {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < M; j++)
					
					if(map[i][j] == 1) {
						
						System.out.println((i + 1) + " " + (j + 1));
						return;
					}
			}
		}
		
		if(isHor && isVer) System.out.println(etcHor + " " + etcVer);
		else if(isHor)
			for(int i = 0; i < res; i++)
				System.out.println(etcHor + " " + (crossHor - (K - 1) + i) );
		else if(isVer)
			for(int i = 0; i < res; i++)
				System.out.println((crossVer - (K - 1) + i) + " " + etcVer);
	}
	
	private static int map[][];
}
