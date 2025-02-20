# bfs(그래프) + dp(최소갱신)
# 직선도로, 코너 최소 비용계산
# Q1. 직선도로, 코너를 어떻게 계산할 것인가
# A1. if 방향이 상 -> 하, 하-> 상, 좌->우, 우->좌 일땐 직선(100), else 코너(600) -> 엥 이거 어케 하지...
# 벽은 피해서 최소비용을 찾아라 
# 디피 필요없지? 그냥 bfs하면 될것 같아 -> 아니면~ 무한대 배열로 초기화 해서 계속해서 최소거리로 갱신

from collections import deque


def solution(board):
    
    answer = 0

    

    # 인덱스 0<->1 , 2<->3 은 직선거리 100원
    # 나머지는 코너 500원 
    # prev_direct
    # curr_direct
    
    
    
    
    
    def bfs(start):
        
        # 북, 동, 남, 서
        direct = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
        n = len(board)
        visited = [[987654321]*n for _ in range(n)]
        visited[0][0] = 0
    
        q = deque([start]) #x,y,cost,direct 저장

        
        while q:
            x,y,cost,d = q.popleft()

            # 상 하 좌 우 순서
            # 북 남 동 서
            for i in range(4):
                nx = x+direct[i][0]
                ny = y+direct[i][1]
                
                
                if 0<= nx < n and 0<= ny < n and board[nx][ny] != 1 :
                    
                    # 비용계산
                    # 직선도로인경우
                    if i == d :
                        ncost = cost + 100
                    # 코너의 경우 (100+회전가중치)
                    else:
                        ncost = cost + 600
                    # 더 작은 비용에 대해서만 갱신해준다.
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append((nx,ny,ncost,i))
        # 마지막요소 출력
        return visited[-1][-1]
    
    # 시작은 동 or 남으로 가는 두가지 경우 존재
    answer = min(bfs((0,0,0,1)),bfs((0,0,0,2)))
    
    return answer

"""
    review: 진짜 크게 착각한 부분은 상<->하, 좌<->우는 100원이 드니까 그 부분을 구현하려고 했단 것이다. 사실은 상,하, 좌,우를 왔다갔다 할 일이 없음(최소거리) 상->하, 좌->우 가되는 경우는 코너를 돌아 방향전환을 하는 방법뿐이므로 이전과 같은 direct을 유지하는게 아니라면 무조건 코너비용이 추가된다는 것이다...!!!! 
    
    또 하나 알게된 점은 나는 이전 방향, 현재 방향 변수를 만들어서 업데이틀 하는 법을 활용하려고했는데 그냥 큐에 저장할때 (좌표,거리,방향)을 한번에 저장해두면 유용하단 것이다...
   
   또한 최소 거리를 유지하는 것이 핵심이므로 무한대로 방문배열을 초기화해두고, 더 작은 값에 대해서만 갱신해주면 된다.(다익스트라처럼)

"""