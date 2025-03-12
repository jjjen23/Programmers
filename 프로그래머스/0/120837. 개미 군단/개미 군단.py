# 장군개미 : 5, 병정개미 : 3, 일개미 : 1
# 최소한의 병력 수를 구하라

def solution(hp):
    answer = 0
    
    how = [5,3,1]
    
    for h in how:
        answer += hp // h
        hp %= h
        if hp <= 0:
            break
        
    
    
    return answer