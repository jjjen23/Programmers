# 돌아가면서 상하좌우탐색 -> 인구이동이 일어난 곳은 체크해두기

n, l, r = map(int, input().split())
answer = 0
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# visited  = [[0]*n for i in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

from collections import deque

def bfs(x,y):
    union = []
    q = deque()
    q.append((x,y))
    union.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if l <= abs(graph[x][y]-graph[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    union.append((nx,ny))
                    q.append((nx,ny))
    if len(union) <= 1:
        return 0
    new_val = 0
    for a,b in union:
        new_val+= graph[a][b]
    new_val = (new_val)//len(union)
    for a,b in union:
        graph[a][b]=new_val
    return 1

day = 0 # 인구이동 날짜를 셀 변수
while True:
    tem = 0 # 인구이동이 일어났는지 체크하는 변수 (==bfs가 일어났는지)
    visited = [[0]*n for _ in range(n)]

    # 전지역을 순환하며 union된 구역이 있는지 체크
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                tem += bfs(i,j)
    if tem > 0:
        day += 1
    else:
        break # 더이상 유니온 될 곳이 없다면 종료(=더 이상 인구이동이 일어날 수 없음)

print(day)