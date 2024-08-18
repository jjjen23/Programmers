def solution(arr):
    answer = 0
    
    # 세 수 a, b, c의 최소공배수 = 두 수 a, b의 최소공배수인 l과 c의 최소공배수 lcm
    # arr의 요소가 2 이상일 때까지 반복
    while len(arr)  > 1:
        
        x_orign = arr.pop()
        y_orign = arr.pop()
        
        x, y = x_orign, y_orign
        
        # gcd 구하기
        while y:
            x, y = y, x % y
        
        # lcm 추가시켜주기
        arr.append((x_orign * y_orign) // x)
        
        
    answer = arr[0]  
    
    return answer