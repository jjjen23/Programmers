# 건물 : 내구도 0 이하 -> 파과
# 건물 : 아군 회복스킬 -> 내구도 상승
# 적의 공격, 아군 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수를 return하라
# skill = [type, r1, c1, r2, c2, degree] 형태로 존재
# type = 1일때 적, 2일때 아군
# (r1,c1) ~ (r2,c2) : 적용 범위
# degree: 공격크기, 회복크키


def solution(board, skill):
    answer = 0
    graph = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    # print(graph)
    
    for skil in skill:
        type, r1, c1, r2, c2, degree = skil
        
        # 1이면 degree를 마이너스 값으로 바꿔준다.
        if type == 1:
            degree = - degree
        
        graph[r1][c1] += degree
        graph[r2+1][c2+1] += degree
        graph[r1][c2+1] -= degree  
        graph[r2+1][c1] -= degree  

    
    # 위에서 아래로 누적합
    for i in range(1,len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] += graph[i-1][j]

    # 왼->오 누적합
    for i in range(len(graph)):
        for j in range(1,len(graph[0])):
            graph[i][j] += graph[i][j-1]
            

    # board와 더해줌
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + graph[i][j] > 0:
                answer += 1
    
    
    return answer

"""
    review: 누적합 개념을 이용해서 시간 효율을 O(1)을 만들어야하는게 관건인데 부르트 포스를 이용함 -> 부르트 포스 방법으로는 쉽게 코드를 짤 수 있었음!! 
    2차원 누적합은 어렵구나. . . 새로 배워갑니다.

# 효율성 실패 코드 #부르트포스
def solution(board, skill):
    answer = 0
    
    for skil in skill:
        type, r1, c1, r2, c2, degree = skil
        if type == 1 :
            for x in range(r1,r2+1):
                for y in range(c1,c2+1):
                    board[x][y] -= degree
        else:
             for x in range(r1,r2+1):
                for y in range(c1,c2+1):
                    board[x][y] += degree     
                    
    for row in board:
        for e in row:
            if e > 0:
                answer += 1
    
    return answer
"""