def solution(n,a,b):
    answer = 1
    
    while n > 1:
        # 해당 라운드에서 A와 B가 붙으면 정답 출력하기
        for i in range(1,n+1,2):
            if (a == i and b == i+1) or (b == i and a == i+1):
                return answer
        
        # 해당 라운드에서 붙지 않는다면, 다음 라운드로 gogo..
        answer += 1
        n //= 2

        if a % 2 == 0:
            a //= 2
        else :
            a = (a+1) // 2

        if b % 2 == 0:
            b //= 2
        else :
            b = (b+1) // 2
        
    return answer