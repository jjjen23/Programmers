def solution(price):
    answer = price
    if price >= 100000 and price < 300000:
        answer *= 0.95
        
    elif price >= 300000 and price < 500000:
        answer *= 0.90
        
    elif price >= 500000:
        answer *= 0.80
        
    
    return int(answer)