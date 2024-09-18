from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    #print(vistited)
    
    queue = deque([(0,0)])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        # print(x,y)
        
        # 네가지 방향전환
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    print(nx,ny)
                    visited[nx][ny] += visited[x][y] + 1 # 이동 가능한 칸마다 해당 칸까지의 길이를 기록해둔다.
                    
    # print(visited[len(maps)-1][len(maps[0])-1])
    if visited[len(maps)-1][len(maps[0])-1] == 0:
        answer = -1
    else:
        answer = visited[len(maps)-1][len(maps[0])-1]
        
    
    return answer