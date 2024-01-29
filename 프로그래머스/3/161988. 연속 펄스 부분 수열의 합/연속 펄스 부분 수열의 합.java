class Solution {
    public long solution(int[] sequence) {
        
        long answer = 0;
        int trigger = -1, seqSize = sequence.length;
        
        // 2 종류의 펄스 수열 초기화
        int[] arr1 = new int[seqSize];
        int[] arr2 = new int[seqSize];
        
        for(int i = 0; i < seqSize; ++i) {
            
            arr1[i] = sequence[i] * trigger;
            arr2[i] = sequence[i] * (trigger *= -1);
        }
        
        // 이전 최대값 + 현재값과 현재값 중에 큰 값을 채택하는 DP
        long[] dp1 = new long[seqSize];
        long[] dp2 = new long[seqSize];
        
        dp1[0] = arr1[0]; dp2[0] = arr2[0];
        answer = Math.max(dp1[0], dp2[0]);
        
        for(int i = 1; i < seqSize; ++i) {
        
            dp1[i] = Math.max(dp1[i - 1] + arr1[i], arr1[i]);
            dp2[i] = Math.max(dp2[i - 1] + arr2[i], arr2[i]);
            
            answer = Math.max(answer, Math.max(dp1[i], dp2[i]));
        }
        
        return answer;
    }
}