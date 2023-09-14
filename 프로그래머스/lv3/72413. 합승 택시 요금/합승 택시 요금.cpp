#include <string>
#include <vector>

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    
    int answer = 20000000;

    vector<vector<int>> minRoute(n + 1, vector<int>(n + 1, 20000000));
    
    for(int i = 0; i < fares.size(); i++) {
        
        minRoute[fares[i][0]][fares[i][1]] = fares[i][2];
        minRoute[fares[i][1]][fares[i][0]] = fares[i][2];
    }
    
    for(int i = 1; i <= n; i++) {
        
        minRoute[i][i] = 0;
    }
    
    for(int k = 1; k <= n; k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                
                if(minRoute[i][j] > minRoute[i][k] + minRoute[k][j])
                    minRoute[i][j] = minRoute[i][k] + minRoute[k][j];
            }
        }
    }
    
    for(int i = 1; i <= n; i++) {
        
        if(answer > minRoute[s][i] + minRoute[i][a] + minRoute[i][b])
            answer = minRoute[s][i] + minRoute[i][a] + minRoute[i][b];
    }
    
    return answer;
}