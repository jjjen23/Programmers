from collections import deque

def solution(m, n, puddles):
    answer = 0
    
    # 웅덩이는 0개 이상 10개 이하
    # 물에 잠긴 지역을 피해 학교까지 최단경로의 수 구하기
    # 오른쪽, 아래쪽으로만 움직일 수 있음.
    dp = [[0]*(m+1) for i in range(n+1)]
    
    dp[1][1] = 1
    # 새칸 = 바로 위 칸 경로 수 + 바로 왼쪽 칸 경로 수 
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                continue
            if [j,i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])  %  1000000007 
    
    
    answer = dp[n][m]
    
    
    return answer