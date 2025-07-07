def solution(n):
    answer = 0
    
    # 약수의 개수가 세 개 이상인 수 = 합성수
    # 2~n까지의 합성수의 개수를 리턴하라.........

    
    for i in range(3,n+1): # 1,2는 약수가 2
        for j in range(2,i): # 1과 자기자신 i는 무조건 나눠짐 -> 나,1제외 
            if i % j == 0:
                answer += 1
                break
    
    
    
    return answer