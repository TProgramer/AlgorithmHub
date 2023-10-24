#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;

    vector<vector<pair<int, int>>> graph(N + 1);
    for(auto ro : road) {
        
        graph[ro[0]].push_back({ro[1], ro[2]});
        graph[ro[1]].push_back({ro[0], ro[2]});
    }
    
    vector<int> dist(N + 1, 20000000);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> pq;
    pq.push({0, 1});
    dist[1] = 0;
    
    while(!pq.empty()) {
        
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();
        
        if(dist[now] < cost) continue;
        
        for(int i = 0; i < graph[now].size(); i++) {
            
            int newCost = cost + graph[now][i].second;
            if(newCost < dist[graph[now][i].first]) {
                
                dist[graph[now][i].first] = newCost;
                pq.push({newCost, graph[now][i].first});
            }
        }
    }
    
    for(int i = 1; i < dist.size(); i++) {
        
        if(dist[i] <= K) answer++;
    }
    return answer;
}