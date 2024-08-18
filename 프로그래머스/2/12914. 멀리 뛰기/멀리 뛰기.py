from itertools import permutations
# 한 칸 -> 1
# 두 칸일때 (1,1) (2) -> 2
# 세 칸일 때 (2,1),(1,2),(1,1,1) -> 3
# 네 칸일 때 -> 5 (두칸 + 세칸)
# 다 섯칸 -> (1,1,1,1,1), (2,1,1,1,1) * 5 , (2,2,1,1,1) 

def solution(n):
    
    dp = [0] * (n+1)
    dp[1] = 1
    
    
    if n >= 2 :
        
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
            
    
    answer = dp[n] % 1234567
        
    
    return answer

# def solution(n):
#     visited = [0] * (n+1)
#     maximum = 2000
#     answer = 0
#     # onelist = [1]*n
#     queue = [0]
#     visited[0] = 1
    
#     while queue:
#         k = queue.pop(0)
#         #visited[k] = 1
        
#         if k == n:
#             answer += 1
            
#         for i in [k+1, k+2]:
#             if i <= n and not visited[i]:
#                 visited[i] = 1
#                 queue.append(i)
    
#     return answer