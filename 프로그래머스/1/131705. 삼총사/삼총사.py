# 조합 모듈 사용
from itertools import combinations

def solution(number):
    answer = 0
    
    triples = list(combinations(number, 3))
    
    for triple in triples:
        if sum(triple) == 0:
            answer += 1
            
    return answer