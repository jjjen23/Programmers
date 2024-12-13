from math import sqrt 

def solution(m, n, startX, startY, balls):
    answer = []
    x,y = m,n
    
    # 공이 목표에 맞을때 까지 최소값의 제곱
    # 공이 맞기 전에 멈추지 않고 공에 맞으면 멈춘다.
    # 친 공이 반사되는 벽을 기준으로 맞을 공의 위치를 대칭시킨 다음 두 공 사이의 직선 거리를 구한다!!
    for ballx, bally in balls:
        tem = []
        # 위쪽 벽
        if not (startX == ballx and startY < bally):
            dist = (ballx - startX)**2 + (2*y-startY-bally)**2
            tem.append(dist)
        # 아래쪽 벽
        if not (startX == ballx and startY > bally):
            dist = (ballx - startX)**2 + (bally+startY)**2
            tem.append(dist)
        # 오른쪽 벽
        if not (bally == startY and ballx > startX):
            dist = (2*x-startX-ballx)**2 + (bally-startY)**2
            tem.append(dist)
        # 왼쪽 벽
        if not (bally == startY and ballx < startX):
            dist = (ballx+startX)**2 + (bally-startY)**2
            tem.append(dist)

        answer.append(min(tem))
        
    return answer