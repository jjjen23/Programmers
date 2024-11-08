from collections import Counter
# 카운터는 존재하지 않는 key값에 대해 에러가 아니라 0을 반환

def solution(weights):
    answer = 0
    # 1. 두 사람의 몸무게가 동일 할 때
    # 2. 다르면 거리*몸무게가 같을 때 (짝 파트너가 하나 이상일 수 있음.)
    counter = Counter(weights)
    # print(counter)
    for c in counter:
        if counter[c] > 0:
            # 두 사람의 몸무게가 동일 할 때 nC2
            answer += counter[c] * (counter[c] - 1) // 2
            # 다를 때
            answer += counter[c] * counter[c*4/3]
            answer += counter[c] * counter[c*4/2]
            answer += counter[c] * counter[c*3/2]
    
    
    return answer