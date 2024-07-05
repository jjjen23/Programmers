import math 

def solution(n):
    answer = -1
    x = int(math.sqrt(n)) #제곱근 구하기
    if x*x == n :
        answer = (x+1) ** 2 #제곱 구하기

    
    return answer

print(solution(121))
print(solution(3))
