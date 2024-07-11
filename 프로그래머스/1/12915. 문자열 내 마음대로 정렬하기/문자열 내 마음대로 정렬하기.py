def solution(strings, n):
    
    # 정렬 우선순위 : n번째 인덱스 -> 사전순서
    answer = sorted(strings, key=lambda x : (x[n], x))
    
    return answer