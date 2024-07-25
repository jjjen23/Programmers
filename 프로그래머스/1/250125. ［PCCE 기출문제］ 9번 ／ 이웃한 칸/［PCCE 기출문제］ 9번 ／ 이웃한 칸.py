def solution(board, h, w):
    answer = 0
    row = len(board)
    col = len(board[0])
    # 상 -> 우 -> 좌 -> 하
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    
    now_color = board[h][w]
    
    for i in range(4):
        h_check = h+dx[i]
        w_check = w+dy[i]
        if 0 <= h_check < row and 0<= w_check < col:
            if board[h_check][w_check] == now_color:
                answer += 1
    return answer