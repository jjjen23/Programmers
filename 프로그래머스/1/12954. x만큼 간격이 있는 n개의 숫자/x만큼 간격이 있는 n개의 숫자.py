def solution(x, n):
    answer = []
    tem = 0
    for i in range(n):
        tem+=x
        answer.append(tem)        
    return answer