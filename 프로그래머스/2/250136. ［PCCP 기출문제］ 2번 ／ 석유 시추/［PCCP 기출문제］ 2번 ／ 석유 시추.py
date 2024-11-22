from collections import deque

def solution(land):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    col = len(land[0])
    row = len(land)
    
    answer = 0
    
    # 각 열에 저장된 석유 양
    result = [0] * col
    visited = [[0]*col for _ in range(row)]
    
    def bfs(x,y):
        q = deque([(x,y)])

        visited[x][y] = 1
        cnt = 1

        oil_covered = set()
        oil_covered.add(y)

        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx <row and 0<=ny<col and visited[nx][ny] == 0:
                    if land[nx][ny] == 1:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                        cnt += 1
                        oil_covered.add(ny)

        for c in oil_covered:
            result[c] += cnt
    
    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                
    answer = max(result)
    
    return answer