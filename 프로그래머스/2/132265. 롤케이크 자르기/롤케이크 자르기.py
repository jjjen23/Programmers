from collections import Counter

def solution(topping):
    answer = 0
    # 슬라이스 횟수 감소
    
    m1 = set()
    m2 = Counter(topping)
    
    for ping in topping:
        m1.add(ping)
        m2[ping] -= 1
        
        if m2[ping] == 0:
            del m2[ping]
        
        if len(m1) == len(m2):
            answer += 1

    return answer