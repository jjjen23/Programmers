n,m = map(int, input().split())

# 관건은 어디에 벽을 3개 세울 것인지 -> 전부 탐색
# 안전영역의 개수가 가장 커지도록 벽을 세워야하고, 그때의 안전영역 수를 출력
# 0은 빈 칸, 1은 벽, 2는 바이러스

from itertools import combinations
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,tem):
    q = deque([(x,y)])

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i], cy+dy[i]
            if 0<=nx<n and 0<=ny<m and tem[nx][ny] == 0:
                tem[nx][ny] = 2
                q.append((nx,ny))

safe, virus, lab = [], [], []
combs = []
temp = [[0]*m for i in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        if data[j] == 0:
            safe.append((i,j))
        elif data[j] == 2:
            virus.append((i,j))
    lab.append(data)

for i in combinations(safe,3):
    combs.append(i)

res = []
for comb in combs:
    # 기존 연구실 구조 복사뜨기
    for i in range(n):
        for j in range(m):
            temp[i][j] = lab[i][j]

    for i in range(3):
        tx,ty = comb[i][0], comb[i][1]
        temp[tx][ty] = 1

    # 바이러스퍼트리기
    for i in virus:
        bfs(i[0],i[1],temp)

    safecnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
               safecnt += 1
    res.append(safecnt)

print(max(res))


