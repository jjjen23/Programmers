import heapq

def solution(n, edge):
    answer = 0
    
    INF = int(1e9)
    
    # 1번 노드에서 가장 멀리 떨어진 노드(갯수 출력)  = 다익스트라 알고리즘 이용!!
    # max 구해서 max와 일치하는 수 카운트
    
    graph = [[] for i in range(n+1)] # 2차원 그래프 생성
    distance = [INF] * (n+1)
    
    for e in edge:
        a,b = e
        graph[a].append((b,1))
        graph[b].append((a,1))
    
    
    queue = []
    
    def dijkstra(start):
        
        
        heapq.heappush(queue,(0,start))
        distance[start] = 0
        
        while queue:
            dist,now =  heapq.heappop(queue)
            
            if distance[now] < dist:
                continue
                
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue,(cost,i[0]))
    dijkstra(1)
    
    max_dist = 0
    for dist in distance:
        if dist != INF and  max_dist < dist:
            max_dist = dist
    print(max_dist)
    
    answer = distance.count(max_dist)
    
    
    return answer