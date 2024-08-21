def solution(n,a,b):
    answer = 1
    # MAX = max[A,B]
    # MIN = min[A,B]
    
    while n > 1:
        for i in range(1,n+1,2):
            if (a == i and b == i+1) or (b == i and a == i+1):
                return answer
        
        
        answer += 1
        n //= 2

        if a % 2 == 0:
            a //= 2
        else :
            a = (a+1) // 2

        if b % 2 == 0:
            b //= 2
        else :
            b = (b+1) // 2
        
    return answer