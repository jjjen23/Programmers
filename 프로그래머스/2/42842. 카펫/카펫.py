def solution(brown, yellow):
    answer = []
    
    i = 0
    while True:
        i += 1
        
        col = i
        # 나누어 떨어지는 수만 !! test!!
        if yellow % i  == 0:
            row = yellow // i
        # 나누어 떨어지지 않는다면 다음 .. 
        else:
            continue

        
        if ((col+2) * (row+2)) - yellow == brown:
            answer.append(row+2)
            answer.append(col+2)
            break
            

    
    return answer