def solution(n):
    ans = 0
    
    # 짝수 홀수..
    while n != 0:
        if n % 2 == 0 :
            n //= 2
        else:
            n -= 1
            ans += 1
    
    

    return ans