#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    unordered_map<string, int> um;
    
    for(auto cloth : clothes) {
        
        if(um.count(cloth[1]) == 1) um[cloth[1]]++;
        else um.insert(make_pair(cloth[1], 1));
    }
    
    int answer = 1;
    for(auto el : um)
        answer *= (el.second + 1);
    
    return answer - 1;
}