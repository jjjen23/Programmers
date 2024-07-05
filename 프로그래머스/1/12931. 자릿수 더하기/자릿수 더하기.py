def solution(n):
    answer = 0
    n_list = list(str(n))
    for i in n_list:
        answer += int(i)
    
    
    return answer