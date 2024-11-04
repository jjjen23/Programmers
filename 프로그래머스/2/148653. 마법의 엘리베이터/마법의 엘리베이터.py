def solution(storey):
    answer = 0
    
    # 중요한건 각 자리수의 값이다. (1의 자릿수만 생각)
    # 현재 자릿값이 6~9 -> 10에 도달하는 쪽
    # 현재 자릿값이 0~4 -> 0에 도달하는 쪽
    # 현재 자릿값이 5 -> 다음자릿수 보고 똑같이
    
    # 0이 되면 종료 
    while storey:
        remainder = storey % 10
        if remainder > 5:
            answer += (10-remainder)
            storey += 10 #다음 자릿수 up
        elif remainder < 5:
            answer += remainder
        # 5일 때
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        # 다음 자릿수로    
        storey //= 10
        print(storey)
        
    
    return answer

print(solution(89))