from collections import deque

def solution(elements):
    answer = 0
    setanswer = set()
    originlen = len(elements)
    elements = elements * 2 # 리스트를 두 개 붙여 원형리스트처럼 사용
    
    for i in range(1, originlen+1):
        for j in range(originlen):
            setanswer.add(sum(elements[j:j+i]))
    answer = len(setanswer)
    
    return answer