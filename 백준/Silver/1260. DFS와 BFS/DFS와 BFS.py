import sys

input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = []
visited_2 = []

#양방향 그래프 생성
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


#bfs함수 정의
def bfs(v, visited):
  queue = deque()
  queue.append(v)
  visited.append(v)

  while queue:
    node = queue.popleft()
    neighbors = sorted(graph[node])
    for neighbor in neighbors:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.append(neighbor)


#dfs함수 정의
def dfs(v, visited):
  if v not in visited:
    visited.append(v)
    neighbors = sorted(graph[v])
    for neighbor in neighbors:
      dfs(neighbor, visited)


dfs(v, visited_2)
for i in visited_2:
  print(i, end=' ')
print()

bfs(v, visited)
for i in visited:
  print(i, end=' ')
