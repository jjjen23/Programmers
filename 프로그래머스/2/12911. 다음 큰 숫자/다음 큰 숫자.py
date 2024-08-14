def solution(n):
    answer = 0
    origin = n
    
    #print(bin(origin)[2:].count('1'))
    # print(bin(origin)[2:])
    while True:
        n+=1
        if bin(origin)[2:].count('1') == bin(n)[2:].count('1'):
            answer = n
            break
    return answer