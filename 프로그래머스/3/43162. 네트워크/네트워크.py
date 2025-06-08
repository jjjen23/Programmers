from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n #노드 수만큼 방문 체크 배열 생성
    
    def bfs(node):
        q = deque([node])
        visited[node] = 1
        
        while q:
            nnode = q.popleft()
            for i in range(n):
                if computers[nnode][i] == 1 and visited[i] != 1:
                    visited[i] = 1
                    q.append(i)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer

"""
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0]*n
    # print(visited)
    # dx = [0,0,1,-1]
    # dy = [1,-1,0,0]
    
    def bfs(node):
        dq = deque([node])
        visited[node] = 1
        
        
        while dq:
            current = dq.popleft()
            
            for i in range(n):
                # 특정 노드와 연결되어 있고, 방문하지 않았다면 -> 방문추가, 큐에 추가 
                if computers[current][i] == 1 and not visited[i]:
                    visited[i] = 1
                    dq.append(i)

    for i in range(n):
        # 방문안된곳 bfs 돌기 -> bfs도는 만큼이 네트워크 수
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer
"""