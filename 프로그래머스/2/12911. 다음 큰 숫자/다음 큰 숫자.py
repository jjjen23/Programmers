def solution(n):
    answer = 0
    origin = n
    
    # print(str(bin(origin)[2:]).count('1'))
    # print(bin(origin)[2:])
    while True:
        n+=1
        if str(bin(origin)[2:]).count('1') == str(bin(n)[2:]).count('1'):
            answer = n
            break
    return answer