class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        
        // 정답 배열 초기화
        int querySize = queries.length;
        int[] answer = new int[querySize];
        
        // 행렬 초기화
        int[][] map = new int[rows + 1][columns + 1];
        
        int count = 1;
        for(int i = 1; i <= rows; ++i) {
            for(int j = 1; j <= columns; ++j) {
             
                map[i][j] = count++;
            }
        }
        
        for(int i = 0; i < querySize; ++i) {
            
            int[] query = queries[i];
            
            int y1 = query[0], x1 = query[1], y2 = query[2], x2 = query[3];
            
            // 현재 위치의 값을 저장 후, 시계방향으로 순차적 옮김
            int now, prev = map[y1][x1], min = Integer.MAX_VALUE;
            
            // 좌상단 -> 우상단 이동
            for(int idx = x1 + 1; idx <= x2; ++idx) {
                
                now = map[y1][idx];
                if(now < min) min = now;
                map[y1][idx] = prev;
                prev = now;
            }
            
            // 우상단 -> 우하단 이동
            for(int idx = y1 + 1; idx <= y2; ++idx) {
                
                now = map[idx][x2];
                if(now < min) min = now;
                map[idx][x2] = prev;
                prev = now;
            }
            
            // 우하단 -> 좌하단 이동
            for(int idx = x2 - 1; idx >= x1; --idx) {
                
                now = map[y2][idx];
                if(now < min) min = now;
                map[y2][idx] = prev;
                prev = now;
            }
            
            // 좌하단 -> 좌상단 이동
            for(int idx = y2 - 1; idx >= y1; --idx) {
                
                now = map[idx][x1];
                if(now < min) min = now;
                map[idx][x1] = prev;
                prev = now;
            }
            
            answer[i] = min;
        }
        
        return answer;
    }
}