# 알고스팟
# 1,1에 있는 운영진이 n,m으로 이동하려면 벽을 최소 몇 개 부숴야 하는지 구하라
# 0은 빈방, 1은 벽을 의미한다.
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
m,n= map(int, input().split())


graph = [list(map(int, input().strip())) for _ in range(n)]
distance = [[INF]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dijkstra():
    q = []
    heapq.heappush(q,(0,0,0)) # 0,0부터
    distance[0][0] = 0
    while q :
        cost, x, y = heapq.heappop(q)

        if cost > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 내에서만
            if 0<= nx < n and 0<=ny<m:
                if cost + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = cost + graph[nx][ny]
                    heapq.heappush(q,(distance[nx][ny],nx,ny))

dijkstra()
print(distance[n-1][m-1])
