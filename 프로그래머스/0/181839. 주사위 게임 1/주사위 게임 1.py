def solution(a, b):

    # 모두 홀수 일때 -> 합이 짝수
    
    # 둘 중 하나만 홀 수 -> 합이 홀수
    
    # 둘 다 짝수일때 -> 합이 짝수
    
    if (a+b) % 2 != 0:
        return 2*(a+b)
    else:
        if a % 2 == 0 and b % 2 == 0:
            return abs(a-b)
        else:
            return a**2 + b **2
