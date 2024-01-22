class Solution {
    public int solution(int n, int k) {
        
        int answer = 0;
        
        String[] split_numbers = Integer.toString(n, k).split("0");
        
        for(String test : split_numbers) {
            
            // 빈 문자열의 경우 제외
            if("".equals(test)) continue;
            
            //10 진수로 돌려서 소수 판별
            long decimal_num = Long.parseLong(test);
            if(isPrime(decimal_num)) answer++;
        }
        
        return answer;
    }
    
    public boolean isPrime(long n) {
        
        if(n < 2) return false;
        
	    for (int i = 2; i <= (int)Math.sqrt(n); i++) {
            
            if (n % i == 0) return false;
	    }  
        
	    return true;
    }
}