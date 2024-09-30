def solution(dirs):
    sets = set()
    x,y = 0,0
    # R L U D
    direct = {'U':(1,0), 'D':(-1,0),'R':(0,1),'L':(0,-1)}
    
    for d in dirs :
        dx, dy = direct[d]
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <=5 and -5 <= ny <=5 :
            
            # 양방향 경로 모두 추가해주기 : 어떤 방향으로 지나 갔든 이미 지나간 경로이기 때문임
            sets.add(((x,y) , (nx, ny)))
            sets.add(((nx,ny) , (x, y)))
            
            x, y = nx, ny
        
    answer = len(sets) // 2
    
    
    
    return answer