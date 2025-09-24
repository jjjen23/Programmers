# 모든 바이러스는 1초마다 상하좌우의 방향으로 증식
# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
# 증식과정에 이미 어떤 바이러스가 존재한다면, 다른 바이러스는 들어갈 수 없다.
# S초가 지난 후에 (x,y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
# 만일 해당 위치에 바이러스가 존재하지 않는 다면 0을 출력한다.
# 상하좌우 한 세트가 1초

n,k = map(int, input().split())
maps = []
viruses = []

for i in range(n):
    data = list(map(int,input().split()))
    maps.append(data)
    for j in range(n):
        if data[j] != 0:
            viruses.append((data[j],0,i,j))


s,x,y = map(int, input().split()) #s초뒤에 종료

from collections import deque

# 바이러스 낮은 순서대로 정렬 후 큐 삽입
viruses.sort()
q = deque(viruses)

dx = [0,0,1,-1]
dy = [1,-1,0,0]


while q:
    virus,time,cx, cy = q.popleft()
    if time == s:
        break

    for i in range(4):
        nx = cx+dx[i]
        ny = cy+dy[i]

        if 0<= nx< n and 0<= ny < n and maps[nx][ny] == 0:
            maps[nx][ny] = virus
            q.append((virus,time+1,nx,ny))

print(maps[x-1][y-1])