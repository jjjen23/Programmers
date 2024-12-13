def solution(board):
    answer = 0
    
    # 예외 처리1 : 하나의 행만 있는 경우 == 세로길이가 1
    if len(board) == 1:
        if 1 in board:
            return 1
    # 예외 처리 2 : 하나의 열만 있는 경우 == 가로길이가 1
    if len(board[0]) == 1:
        if 1 in board[0]:
            return 1
    
    dp = [[0]*(len(board[0])) for _ in range(len(board))]
    # print(dp)
    global_max = 0
    # 첫 행, 첫 열은 초기화해준다.
    for i in range(len(board)):
        dp[i][0] = board[i][0]
    dp[0] = board[0]
    
    # 1열, 1행 이상 부터 탐색, 위, 대각선 위, 왼쪽 탐색 하기 위함
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                
            if dp[i][j] > global_max :
                global_max = dp[i][j] 
                
    answer = global_max ** 2 # 넓이니까 제곱
    
    return answer