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
            # 웅덩이 경로가 뒤집혀 있음
            if [j,i] in puddles:
                # 웅덩이 만나면 경로 초기화 
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])  %  1000000007 
    
    
    answer = dp[n][m]
    
    
    return answer


"""
 review: 1. 문제에서 학교의 좌표는 (m,n)으로 제시 -> 우리가 일반적으로 사용하는 x,y좌표와 반대인 형태 -> 웅덩이 체크시 좌표 뒤집어서 체크해주어야 함
         2. 나는 경로 길이를 구해서 카운트 할 생각을 했는데 경로의 수 자체를 업데이트 하는 방법을 이용한 dp문제 였다.. 똑똑하다..!!!
         3. 이전값을 이용하기 위해 2차원 그래프 길이를 1씩 확장해서 활용하는 모습 -> 문제 의도대로 1,1 좌표부터 시작해도 적절하므로 좋다..
         4. dp는 왤케 겁을먹는건지.. 연습 많이해야겠다..점화식만 잘 찾아보자..
"""