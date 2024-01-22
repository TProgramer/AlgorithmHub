class Solution {
    public int[] solution(int n) {
        
        int answerSize = n * (n + 1) / 2;
        int[] answer = new int[answerSize];
        
        int[][] arr = new int[n][];
        for(int i = 0; i < n; i++) {
            
            arr[i] = new int[i + 1];
        }
        
        arr[0][0] = 1;
        int nowY = 0, nowX = 0, dir = 0, count = 2;
        
        while(true) {
            
            if(count > answerSize) break;
            
            if(dir % 3 == 0) {
                
                if(nowY >= n - 1 || arr[nowY + 1][nowX] != 0) {
                    
                    dir++; nowX++;
                }
                else nowY++;
            }
            
            else if(dir % 3 == 1) {
                
                if(nowX >= n - 1 || arr[nowY][nowX + 1] != 0) {
                    
                    dir++; nowY--; nowX--;
                }
                else nowX++;
            }
                
            else if(dir % 3 == 2) {
                
                if(nowY <= 0 || arr[nowY - 1][nowX - 1] != 0) {
                    
                    dir++; nowY++;
                }
                else {
                    
                    nowY--; nowX--;
                }
            }
                
            arr[nowY][nowX] = count++;
        }
        
        int idx = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i + 1; j++) {
                
                answer[idx++] = arr[i][j];
            }
        }
        
        return answer;
    }
}