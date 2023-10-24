#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    int answer = 0, sum = 0;
    
    priority_queue<int> que;
    for(auto ene : enemy) {
        
        sum += ene;
        que.push(ene);
        if(n < sum) {
            
            if(k == 0) break;
            sum -= que.top();
            que.pop();
            k--;
        }
        answer++;
    }
    
    return answer;
}