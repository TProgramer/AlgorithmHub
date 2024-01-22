class Solution {
    
    public int[] solution(int[][] arr) {
        
        int[] answer = {0, 0};
        
        dac(arr, 0, 0, arr.length, answer);
        
        return answer;
    }
    
    public void dac(int[][] arr, int startY, int startX, int length, int[] answer) {
        
        if(isQuadZipAvailable(arr, startY, startX, length, arr[startY][startX])) {
            
            if(arr[startY][startX] == 0) answer[0]++;
            else answer[1]++;
            
            return;
        }
        
        int newLength = length / 2;
        dac(arr, startY, startX, newLength, answer);
        dac(arr, startY, startX + newLength, newLength, answer);
        dac(arr, startY + newLength, startX, newLength, answer);
        dac(arr, startY + newLength, startX + newLength, newLength, answer);
    }
    
    public boolean isQuadZipAvailable(int[][] arr, int startY, int startX, int length, int checker) {
        
        for(int i = startY; i < startY + length; i++) {
            for(int j = startX; j < startX + length; j++) {
                
                if(arr[i][j] != checker) return false;
            }
        }
        return true;
    }
}