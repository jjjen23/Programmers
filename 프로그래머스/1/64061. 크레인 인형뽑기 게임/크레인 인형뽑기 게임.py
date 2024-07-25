def solution(board, moves):
    answer = 0
    n = len(board)
    banglist = []
    
    for i in moves:
        for j in range(n):
            # 2차원 배열 세로 순회
            if board[j][i-1] != 0:
                doll = board[j][i-1]
                banglist.append(board[j][i-1])
                board[j][i-1] = 0 # 집어넣었으면 0 할당
                
                
                if len(banglist) > 1 :
                    if banglist[-2] == banglist[-1]:
                        answer += 2
                        del banglist[-2:]
                break # 검사하고 다음으로 뽑기로 가도록해주어야 함
                   
                    
                    
    return answer