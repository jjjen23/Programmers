import heapq

def solution(A, B):
    answer = 0
    
    # 숫자가 큰 팀 -> +1
    # 동점 -> 아무일도없었다...
    # B팀의 승점을 가장 높이는 방법으로 출전 순서 정할때 최종 승점 return
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    i = 0
    
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1
    return answer
    

    return answer