def solution(n):
    answer = 0
    dp = [0,1,2]
    
    if n < 3:
        return dp[n]
    
    for i in range(3,n+1):
        dp.append(0)
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
        
    
    answer = dp[n]
        
    return answer