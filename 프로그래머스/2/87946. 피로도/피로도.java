class Solution {
    
    public int answer = 0;
    public int[][] map;
    public boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        
        // 글로벌 변수로 던전을 저장
        map = dungeons;
        
        // DFS에서 방문 여부를 관리할 배열
        visited = new boolean[dungeons.length];
        
        // DFS로 모든 던전들을 임의의 순서로 탐험하며 최대 던전 수를 찾기
        dfs(0, k);
        
        return answer;
    }
    
    public void dfs(int depth, int k) {
        
        for(int i = 0; i < map.length; i++) {
            
            if(!visited[i] && map[i][0] <= k) {
                
                visited[i] = true;
                dfs(depth + 1, k - map[i][1]);
                visited[i] = false;
            }
        }
        
        // 모든 던전을 공략 후, 최다 던전인지 갱신
        answer = Math.max(answer, depth);
    }
}