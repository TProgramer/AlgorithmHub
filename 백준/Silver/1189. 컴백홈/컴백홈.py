import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
info = []
for _ in range(R):
    info.append(list(input().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

# DFS + 백트레킹 조합으로 지나온 길을 지우고 복구하며, 경우의 수 계산
def dfs(x, y, distance):
    global answer
    if distance == K and y == C - 1 and x == 0:
        answer += 1
    else:
        # 그 외에는 방문처리
        info[x][y] = 'T'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(0 <= nx < R and 0 <= ny < C and info[nx][ny] == '.'):
                info[nx][ny] = 'T'
                dfs(nx, ny, distance + 1)
                # 원래 상태로 돌리기
                info[nx][ny] = '.'

dfs(R - 1, 0, 1)
print(answer)