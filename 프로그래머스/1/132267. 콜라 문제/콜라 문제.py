def solution(a, b, n):
    answer = 0
    
    while n >= a:
        reminder = n % a
        exchange = int(n//a) * b
        answer += exchange
        n = exchange + reminder
        
    return answer