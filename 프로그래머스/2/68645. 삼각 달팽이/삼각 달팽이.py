def solution(n):
    answer = []
    tri = [[0]*i for i in range(1,n+1)]
    
    direct = [(1,0),(0,1),(-1,-1)] #(아래 -> 오른쪽 -> 왼쪽 위 대각선)
    turn = 0
    x,y = 0,0
    i = 1
    end_num = sum(i for i in range(1,n+1))
    
    while i <= end_num:
        tri[x][y] = i
        i += 1
        dx, dy = direct[turn]
        nx = x+dx
        ny = y+dy
        
        if 0 <= nx < n and 0<= ny < len(tri[nx]) and tri[nx][ny]==0:
            x,y = nx, ny
        else:
            turn = (turn+1) % 3 #(방향이 세개)
            dx, dy = direct[turn]
            x += dx
            y += dy
            
    for row in tri:
        for i in row:
            answer.append(i)
    
    
    return answer