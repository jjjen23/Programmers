# [lux = 열최소, luy = 행최소 rdx = 열최대, rdy = 행최대]

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

"""
# 샵이 나오는 좌표 다 집어 넣고 최대 최소 구하기

def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i) # row 좌표 저장
                b.append(j) # col 좌표 저장
    return [min(a), min(b), max(a) + 1, max(b) + 1]
    
"""