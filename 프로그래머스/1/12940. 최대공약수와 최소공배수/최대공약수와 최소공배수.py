def solution(n, m):
    x, y = n, m

    # GCD(최대공약수), 유클리드호제법
    while(y):
        x, y = y, x % y
    GCD = x
    # LCM(최소공배수)
    LCM = (n*m) // GCD
    
    answer = [GCD,LCM]
    
    return answer