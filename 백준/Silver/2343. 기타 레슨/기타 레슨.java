import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] lectures = new int[N];
		for(int i = 0; i < N; i++) lectures[i] = sc.nextInt();
		
		int left = 0; int right = N * 10000, ret = 0;
		while (left <= right)
	    {
	        int mid = (left + right) / 2;
	        boolean isPossible = true;
	        
	        int sum = 0, count = 1;
	        for (int i : lectures){
	        	
	            if(i > mid) isPossible = false;
	            if(sum + i <= mid) sum += i;
	            else {
	            	
	                sum = i;
	                count++;
	            }
	        }
	        if(count > M) isPossible = false;
	        
	        if (isPossible)
	        {
	            right = mid - 1;
	            ret = mid;
	            
	        }
	        else {
	            left = mid + 1;
	        }
	    }
		System.out.println(ret);
	}
}