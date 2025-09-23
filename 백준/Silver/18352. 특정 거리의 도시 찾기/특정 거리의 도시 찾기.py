import sys
from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [-1]*(n+1)
def bfs(start):
    q = deque([start])
    visited[start] = 0 #자기자신까지의 거리는 0

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)
bfs(x)

res = []

check = False
for i in range(1,n+1):
    if visited[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)