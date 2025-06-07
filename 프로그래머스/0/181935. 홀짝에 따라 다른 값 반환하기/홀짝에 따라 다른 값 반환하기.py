def solution(n):
    answer = 0
    # n이하의 홀 수 인 모든 양의 정수 합 : 홀수
    
    if n % 2 == 0:
        for i in range(n+1):
            if i % 2 == 0:
                answer += i**2
    else:
        for i in range(n+1):
            if i % 2 !=0 :
                answer += i
                
    return answer