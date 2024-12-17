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
                if computers[current][i] == 1 and not visited[i]:
                    visited[i] = 1
                    dq.append(i)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    
    return answer