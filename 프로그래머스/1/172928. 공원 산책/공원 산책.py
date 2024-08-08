def solution(park, routes):
    
    dict1 = {
        "E" : (0,1),
        "W" : (0,-1),
        "N" : (-1,0),
        "S" : (1,0)
    }
    
    row = len(park)
    col = len(park[0])
    
    for i in range(row):
        flag = False
        for j in range(col):
            if park[i][j] == 'S':
                sx, sy = i , j
                flag = True
                break
        if flag == True:
            break

    
    
    x, y = sx, sy
    
    for route in routes:
        direct, cnt = route.split(" ")
        cnt = int(cnt)
        
        dx, dy = dict1[direct]
        
        flag = False
        tem_x , tem_y = x, y
        
        for _ in range(cnt):
            tem_x += dx
            tem_y += dy
            
            if 0<= tem_x < row and 0<=tem_y <col and park[tem_x][tem_y] != "X":
                flag = False
            else:
                flag = True
                break
        
        if flag == False:
            x, y = tem_x, tem_y
        
        else:
            continue
            
        
    answer = [x,y]
               
    
    return answer


"""
         for _ in range(cnt):
            if direct in dict1:
                dx, dy = dict1[direct]
                nx += dx
                ny += dy
                
                if 0<= nx < row and 0<=ny< col and park[nx][ny] == "O":
                    tem_x, tem_y = nx, ny
                else:
                    flag = True
                    break
                    
        if flag == True:
            continue
        else:
            nx, ny = tem_x, tem_y
"""