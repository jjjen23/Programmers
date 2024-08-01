def solution(wallpaper):
    answer = []
    row = len(wallpaper)
    col = len(wallpaper[0])
    
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    
    
    # lux,luy 찾기
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == '#':
                answer.append(i)
                flag1 = True
                break
        if flag1 :
            break
                
    for j in range(col):
        for i in range(row):
            if wallpaper[i][j] == "#":
                answer.append(j)
                flag2 = True
                break
        if flag2 :
            break
                
    # rdx, rdy 찾기
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            if wallpaper[i][j] == '#':
                answer.append(i+1)
                flag3 = True
                break
        if flag3 :
            break
    
    for j in range(col-1,-1,-1):
        for i in range(row-1,-1,-1):
            if wallpaper[i][j] == "#":
                answer.append(j+1)
                flag4 = True
                break
        if flag4 :
            break
    
    return answer