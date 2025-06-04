def solution(n):
    answer = [n]
    # 짝수 -> 2
    # 홀수 3*x + 1
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1
        answer.append(n)
    
    return answer