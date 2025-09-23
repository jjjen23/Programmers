from itertools import combinations
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs로 바이러스 전파
def bfs(x,y, temp) :
    q = deque([(x,y)])

    while q :
        cx, cy = q.popleft()
        for i in range (4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx > n-1 or ny < 0  or ny > m-1 or temp[nx][ny] == 1 or temp[nx][ny] == 2:
                continue
            else : 
                temp[nx][ny] = 2 
                q.append((nx, ny))


n, m = map(int, input().split())
lab, safe, virus = [], [], []
temp = [[0] * m for _ in range(n)] # 매번 달라지는 map을 처리해주는 행렬 초기화
results = []

for x in range(n) :
    data = list(map(int, input().split()))
    for y in range (m) :
        if data[y] == 0 :
            safe.append((x,y))
        elif data[y] == 2:
            virus.append((x,y))
    lab.append(data)

walls = []
# 가능한 조합 검사
for i in combinations(safe, 3):
    walls.append(i)

for wall in walls :
    safecnts = 0 # 0의 개수
    # 맵 정보 복사
    for i in range (n) :
        for j in range(m) :
            temp[i][j] = lab[i][j] # temp = lab은 안된다.
    #  가능한 조합을 순회하며 벽 설치
    for w in range(3) :
        wx, wy = wall[w][0], wall[w][1]
        temp[wx][wy] = 1
    for v in virus :
        vx, vy = v[0], v[1]
        bfs(vx, vy, temp) # 바이러스 퍼트리기
    # 매 조합마다 안전영역(0)의 개수 세서 정보 저장
    for i in range (n) :
        for j in range(m):
            if temp[i][j] == 0 :
                safecnts+=1
    results.append(safecnts)

# 가장 큰 값 출력
print(max(results))
