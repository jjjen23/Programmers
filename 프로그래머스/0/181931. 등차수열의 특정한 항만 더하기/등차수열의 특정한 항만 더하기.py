def solution(a, d, included):
    if included[0] :
        answer = a
    else:
        answer = 0
        
    for i in range(1, len(included)):
        if included[i]:
            answer += (a + d*i)
    return answer