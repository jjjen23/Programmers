from math import sqrt, ceil, floor

def solution(r1, r2):
    answer = 0
    
    # total = 한 사분면만 구해서 * 4
    for x in range(1, r2+1) :
        # x가 정수일 때 y가 정수인 점을 탐색
        y2 = floor(sqrt(r2**2-x**2))
        y1 = ceil(sqrt(max(0,r1**2-x**2)))
        answer += y2-y1 +1
    answer = answer * 4
    
    
    return answer