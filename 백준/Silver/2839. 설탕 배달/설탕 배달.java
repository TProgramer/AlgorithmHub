import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(), count = 0;
		
		while(N >= 0) {
			
			if(N % 5 == 0) {
				
				System.out.println(count + (N / 5));
				return;
			}
			N -= 3;
			count++;
		}
		System.out.println(-1);
	}

}
