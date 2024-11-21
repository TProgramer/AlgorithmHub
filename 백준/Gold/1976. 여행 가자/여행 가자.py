import sys
input = sys.stdin.readline

# 유니온파인드로 모든 노드의 부모 계산 후, 모두 방문 가능한지 확인
def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# 입력값 받기
n,m = int(input()),int(input())
parents = [i for i in range(n)]
for i in range(n):
    link = list(map(int,input().split()))
    for j in range(n):
        if link[j] == 1:
            # 연결된 경로에 대해 유니온파인드 시행
            union(i,j)

# 방문 가능여부 확인
path = list(map(int,input().split()))
start = parents[path[0] - 1]
for i in range(1,m):
    if parents[path[i] - 1] != start:
        print("NO")
        break
else:
    print("YES")