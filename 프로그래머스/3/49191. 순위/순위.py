# 플로이드-워셜 알고리즘: 모든 노드 쌍 간 최단 거리
#  체크되지 않은 값이 1개인 경우 -> 순위결정

def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    # 그래프에 기존 정보 입력
    for a,b in results:
        # a는 b를 이긴다.
        board[a-1][b-1] = 1 #이김 표시
        board[b-1][a-1] = -1 # 짐 표시
    
    # 특정한 노드 k를 거쳐 가는 거리와 a->b거리 중 짧은 것으로 갱신
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 나 자신 -> 자신인 경우와 이미 갱신된 것은 컨티뉴
                if i == j or board[i][j] in [1,-1]:
                    continue
                # i가 k를 이겼어, 그리고 k가 j를 이겼어 -> i는 j를 이겨를 기록, 그 반대는 -1 기록
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    
    for b in board:
        if b.count(0) == 1:
            answer += 1
            
    
    return answer