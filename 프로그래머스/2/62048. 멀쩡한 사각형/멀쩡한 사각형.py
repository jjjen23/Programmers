# 최대공약수
def gcd(x,y):
    while y > 0:
        x,y = y, x%y
    return x
        
        

def solution(w,h):
    answer = 1
    total = w*h
    GCD = gcd(w,h)
    answer = total - (w+h-GCD)
    
    return answer