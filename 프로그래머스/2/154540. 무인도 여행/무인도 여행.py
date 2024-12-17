from collections import deque

def solution(maps):
    answer = []
    
    # 각 섬에서 최대 며칠씩 머무를 수 있는지 오름차순 정렬
    # 섬이 존재하지 않는 다면 -1
    
    m = len(maps[0])
    n = len(maps)
    visited = [[0] * m for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    def bfs(x,y):
        visited[x][y] = 1
        days = int(maps[x][y])
        q = deque([(x,y)])
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx < n and 0<= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = 1
                    days += int(maps[nx][ny])
                    q.append((nx,ny))
        return days
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i,j))
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer