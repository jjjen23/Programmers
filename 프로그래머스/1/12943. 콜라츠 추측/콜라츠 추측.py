def solution(num):
    # 주어진 수가 1인 경우에 0 반환
    if num == 1:
        return 0
    
    cnt = 0
    
    # 주어진 수가 1이 될 때 까지 작업 반복
    while num !=1: 
        # 만일 작업을 500번 반복했다면 -1 반환
        if cnt == 500:
            return -1
        
        if num % 2 == 0:
            num /= 2
            cnt += 1
        else:
            num = (num * 3)+1  
            cnt += 1
    
    answer = cnt
    
    return answer