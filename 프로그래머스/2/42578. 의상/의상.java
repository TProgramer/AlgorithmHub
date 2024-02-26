import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        
        int answer = 1;
        
        // 옷의 종류 개수를 저장하는 해쉬맵
        HashMap<String, Integer> clothCount = new HashMap<>();
        
        // 전체 옷 배열을 순회하며
        for(String[] cloth : clothes) {
            
            // 옷의 종류에 따라 해쉬맵에 카운트
            String category = cloth[1];
            if(clothCount.containsKey(category)) {
                
                int count = clothCount.get(category);
                clothCount.replace(category, ++count);
            }
            else {
                clothCount.put(category, 1);   
            }
        }
        
        Collection<Integer> values = clothCount.values();
        for(Integer value : values) {
            
            answer *= (value + 1);
        }
        
        return answer - 1;
    }
}