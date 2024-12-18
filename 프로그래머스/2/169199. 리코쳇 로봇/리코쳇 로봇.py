from collections import deque

def solution(board):
    answer = 0
    
    # R 좌표 출력
    # dfs(r1,r2) 정의
    # 장애물이나 판의 경계에 도달시 +1
    # 시작 -> 목표까지 몇번 이동하는지 카운트
    # 도달할 수 없다면 -1 리턴
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    m = len(board[0])
    n = len(board)
    
    visited = [[0]*m for _ in range(n)]
    
    
    def bfs(x,y):
        visited[x][y] = 1
        queue = deque([(x,y)])
        
        
        while queue:
            x,y = queue.popleft()
            
            if board[x][y] == 'G':
                return visited[x][y] - 1
            
            for i in range(4):
                nx, ny = x,y
                
                # 범위 내이고, D가 아니라면 전진(D를 만나기 직전까지~!)
                while 0<= nx+dx[i] <n and 0<= ny+dy[i]< m and board[nx+dx[i]][ny+dy[i]] != 'D':
                    nx += dx[i]
                    ny += dy[i]
                    
                # 직전 좌표에 방문 체크하고, 기존 거리에 1 더해주기, 직전 좌표부터 재탐색 시작.
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
        return -1
                    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer= bfs(i,j)
                print(visited)
                break
            
    
    return answer