import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        // scoville 배열의 원소들을 힙에 추가
        for(Integer scovil : scoville) {
            
            pq.offer(scovil);
        }
        
        // while 문을 돌며 최소값이 K 이상이 될 때까지 새로운 음식 만들기
        while(pq.peek() < K) {
            
            // 만약 마지막 원소만 남았다면 -1을 리턴;
            if(pq.size() == 1) return -1;
            
            int sco1 = pq.poll();
            int sco2 = pq.poll();
            
            int newSco = sco1 + sco2 * 2;
            
            pq.offer(newSco);
            answer++;
        }
        
        return answer;
    }
}