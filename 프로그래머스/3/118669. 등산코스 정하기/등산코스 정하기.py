from math import inf
import heapq

def solution(n, paths, gates, summits):
    
    # 다익스트라 알고리즘을 활용하여 하나의 출입구와 하나의 산봉우리간의 경로에서
    # 지나가는 모든 가중치의 값의 최대값이 가장 작은 경로의 산봉우리와 최대 가중치 찾기
    
    # 간선 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
        
    # 다익스트라 알고리즘 활용
    distance = [inf] * (n + 1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, (0, gate))
        
    while queue:
        nowDist, nowLoc = heapq.heappop(queue)
        
        # 만약 산봉우리를 만나면, 다른 산봉우리를 방문하지 않도록 continue
        if distance[nowLoc] < nowDist or nowLoc in summits:
            continue
            
        for nextLoc, nextDist in graph[nowLoc]:
            # 현재까지의 intensity와 다음 거리 중 큰 값이 다음 intensity보다 작다면 최단거리 갱신
            maxDist = max(distance[nowLoc], nextDist)
            if distance[nextLoc] > maxDist:
                distance[nextLoc] = maxDist
                heapq.heappush(queue, (maxDist, nextLoc))
                
    # intensity가 같다면 작은 수의 산봉우리 반환
    maxDist = inf
    answer = ()
    for summit in sorted(summits):
        if distance[summit] < maxDist:
            answer = (summit, distance[summit])
            maxDist = distance[summit]
    
    return answer