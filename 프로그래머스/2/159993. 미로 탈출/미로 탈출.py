from collections import deque

def bfs(maps, startInfo, endInfo):
    
    # 4방향 체크를 위한 방향 배열
    direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 맵의 크기 정보
    row = len(maps)
    col = len(maps[0])
    
    # 방문 여부 배열
    visited = [[False] * col for _ in range(row)]
    
    startY, startX = startInfo
    queue = deque([(startY, startX, 0)])
    visited[startY][startX] = True
    while queue:
        nowY, nowX, nowTime = queue.popleft()
        
        if maps[nowY][nowX] == endInfo:
            return nowTime
        
        for i in range(4):
            newY = nowY + direc[i][0]
            newX = nowX + direc[i][1]
            
            # 탐색 가능한 곳인지 확인
            if 0 <= newY < row and 0 <= newX < col and maps[newY][newX] != "X" and not visited[newY][newX]:
                queue.append((newY, newX, nowTime + 1))
                visited[newY][newX] = True
                
    return -1


def solution(maps):
    
    # 총 두번의 BFS로 최소 시간 탐색
    # 1. 출발 지점 -> 레버
    # 2. 레버 -> 출구
    
    # 시작 전, 두 출발지(출발, 레버)의 위치 확인
    startInfo, leverInfo = (), ()
    for idx, row in enumerate(maps):
        start = row.find("S")
        if start != -1: startInfo = (idx, start)
        lever = row.find("L")
        if lever != -1: leverInfo = (idx, lever)
    
    # 각 스텝을 진행 후, 진행 가능 여부 확인
    step1 = bfs(maps, startInfo, "L")
    if step1 == -1: return -1
    step2 = bfs(maps, leverInfo, "E")
    if step2 == -1: return -1
    
    return step1 + step2