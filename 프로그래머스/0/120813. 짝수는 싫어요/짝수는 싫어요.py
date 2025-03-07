def solution(n):
    answer = [1]
    for i in range(2,n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer