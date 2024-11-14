from collections import deque

def FindL(s,maps):
    
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    stack = deque([s])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    
    while stack:
        x,y = stack.popleft()
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                if  maps[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    l = (nx,ny)
                    print(visited[nx][ny])
                    return l, visited[nx][ny]
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    stack.append((nx,ny))
                    
    return -1, -1

def FindE(l,maps):
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    stack = deque([l])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    
    while stack:
        x,y = stack.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                if  maps[nx][ny] == 'E':
                    visited[nx][ny] = visited[x][y] + 1
                    e = (nx,ny)
                    print(visited[nx][ny])
                    return visited[nx][ny]
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    stack.append((nx,ny))
                    
    return -1
    

def solution(maps):
    # 미로탈출 최소시간 반환
    answer = 0
    
    # s 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = (i,j) 
                break
    # print(s)
    
    
    
    l, distanceL = FindL(s,maps)
    print(distanceL)
    
    # findL함수가 -1이면 -1를 리턴하고 종료
    # 아니면 L에서 부터 E까지 다시 bfs
    if l == -1:
        return -1
    else:
        distanceE = FindE(l,maps)
        if distanceE == -1:
            return -1
        else:
            answer = distanceL + distanceE
        
    
    return answer