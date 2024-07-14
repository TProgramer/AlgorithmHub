from collections import deque

def solution(maps):
    
    # map의 row, col 크기
    maps_row = len(maps)
    maps_col = len(maps[0])
    
    # BFS로 최단거리 탐색하기
    queue = deque([((0, 0), 2)])
    
    # 사방향 탐색을 위한 움직임 배열
    dirY = [-1, 1, 0, 0]
    dirX = [0, 0, -1, 1]
    
    while queue:
        
        location, depth = queue.popleft()
        nowY, nowX = location
        
        for direc in range(4):
            newY, newX = nowY + dirY[direc], nowX + dirX[direc]
            
            # 새로운 좌표가 탐색 불가능하다면 스킵
            if newY < 0 or newY >= maps_row or newX < 0 or newX >= maps_col or maps[newY][newX] == 0:
                continue
                
            # 상대 팀 진영에 도착하면, 이동 거리를 반환
            if newY == maps_row - 1 and newX == maps_col - 1:
                return depth
            
            # 현재 블럭 방문처리 후, queue에 추가
            maps[newY][newX] = 0
            queue.append(((newY, newX), depth + 1))
    
    # 끝까지 도착하지 못했다면 -1 반환
    return -1