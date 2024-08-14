def solution(brown, yellow):
    answer = []
    #print(int(yellow**0.5))
    
    
    i = 0
    while True:
        i += 1
        col = i
        if yellow % i  == 0:
            row = yellow // i
        else:
            continue
        #print(col,row)
        
        if ((col+2) * (row+2)) - yellow == brown:
            answer.append(row+2)
            answer.append(col+2)
            break
            
    #answer.sort(reverse = True)
    
    return answer