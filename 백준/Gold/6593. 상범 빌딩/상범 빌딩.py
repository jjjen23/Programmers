# 상범빌딩
# 탈출하는 가장 빠른 길은 무엇일까
# 비어있는칸은 . 막혀있는칸은 #
# 탈출 가능하다면 Escaped in x minute(s).
# 불가능하다면, Trapped!

import sys
from collections import deque
input = sys.stdin.readline

#동서남북상하 6방향 이동가능 == 3차원(정육면체)
dx = (0,0,1,-1,0,0)
dy = (0,0,0,0,1,-1)
dz = (1,-1,0,0,0,0)

# 종료조건 까지 반복
while True:
    l, r, c = map(int, input().split())
    # c개의 문자로 이루어진 R개의 행이 L번 주어진다.

    # 종료조건 충족 시 break
    if l == 0 and r == 0 and c == 0:
        break

    # 3차원 구조물을 입력받아 저장할 배열

    board = []

    #3차원 방문 배열 생성하기
    visited = [[[False]*c for _ in range(r)] for _ in range(l)]
    # 3차원 방문배열 입력받기
    for _ in range(l):
        board.append([list(input().strip()) for _ in range(r)])
        temp = input() # 공백줄을 읽고 무시하는 역할

    q = deque()
    escaped = False # 일단 미탈출로 bool 설정

    # 배열을 돌면서 시작점과 끝점 찾기
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    start = (i,j,k,0)
                    visited[i][j][k] = True
                if board[i][j][k] == 'E':
                    goal = (i,j,k)

    # 시작 3차원 좌표와, 길이(시간) 저장
    q.append(start)

    # bfs실시
    while q :
        z,x,y,d = q.popleft()
        # 목표 좌표라면, escape변수값을 True로 설정하고, 몇 초 걸린지 출력학 뒤 종료
        if (z,x,y) == goal:
            escaped=True
            print(f'Escaped in {d} minute(s).')
            break

        # 6방향 이동 전, 시간 증가
        nd = d+1
        # 6방향 탐색
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내이고, 방문하지 않았다면
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny] :
                # 이동가능한 공간이거나 끝지점이라면 q에 추가하고 방문 업데이트
                if board[nz][nx][ny] == '.' or board[nz][nx][ny] =='E':
                    q.append((nz,nx,ny,nd))
                    visited[nz][nx][ny] = True

    # 만일 전체 bfs탐색 후에, escape가 False라면 탈출 실패의미
    if not escaped:
        print('Trapped!')






