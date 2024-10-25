from collections import deque
def solution(x, y, n):
    answer = 0
    
    if x==y:
        return 0
    
    dp = [-1] * 1000001
    dp[x] = 0
    queue = deque([x])
    
    while queue:
        tem_x = queue.popleft()
        
        for i in [2*tem_x, 3*tem_x, tem_x+n]:
            if i <=y and i <= 1000000:
                if dp[i] == -1:
                    dp[i] = dp[tem_x] + 1
                    queue.append(i)
                    
                    if i == y:
                        return dp[i]
                    
                     
            
        
    return -1