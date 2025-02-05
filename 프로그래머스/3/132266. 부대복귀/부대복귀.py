import heapq

def solution(n, roads, sources, destination):
    
    answer = []
    
    # 그래프, 다익스트라임
    # 복귀 불가능 시 -1 반환
    # sources의 각 요소가 순서대로 -> destination으로 복귀 가능한지, 가능하다면 최단 거리를 answer에 추가, 불가능하다면 -1 추가
    

    INF = int(1e9)
    distance = [INF]*(n+1)
    graph = [[] for i in range(n+1)]
    
    for road in roads:
        x,y = road
        graph[x].append(y)
        graph[y].append(x)
    
    # 출발지 -> 목적지 최단길이 찾아주는 다익스트라 알고리즘 설계 -> 시간초과
    # 개선 : 목적지 -> 출발지 다익스트라 실행시 한번만 다익스트라 수행하면됨;;;
    
    def dijkstra(start):
        q = []
        
        heapq.heappush(q,(0,destination))
        distance[start] = 0
        
        while q:
            dist,now = heapq.heappop(q)
            
            if distance[now] < dist :
                continue
            for i in graph[now]:
                cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q,(cost,i))
    
    # 다익스트라수행
    dijkstra(destination)
    
    # 출발지, 목적지별 최단경로를 추가해준다.
    for s in sources:
        if distance[s] != INF:
            answer.append(distance[s])
        else:
            answer.append(-1)
    
    
    return answer