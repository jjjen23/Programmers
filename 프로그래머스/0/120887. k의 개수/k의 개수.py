def solution(i, j, k):
    answer = 0
    for S in range(i,j+1):
        if str(k) in str(S):
            answer += str(S).count(str(k))
    
    
    return answer