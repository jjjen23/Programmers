def solution(a, b, n):
    answer = 0
    
    # update 해야하는 거 : n 
    # 내가 가진 빈병이 a보다 작으면 종료(더 이상 교환 불가)
    while n >= a:
        remainder = n % a
        exchange = int(n//a) * b
        answer += exchange
        n = exchange + remainder
        
    return answer