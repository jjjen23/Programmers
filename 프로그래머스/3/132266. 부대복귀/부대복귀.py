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
    
    # 출발지 -> 목적지 최단길이 찾아주는 다익스트라 알고리즘 설계 -> 출발지별 다익스트라 다회 수행 -> 시간초과
    # 개선 : 목적지 -> 출발지 다익스트라 실행시 한번만 다익스트라 수행하면 됨;;;
    
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
    
    # 목적지 출발 다익스트라 수행
    dijkstra(destination)
    
    # 목적지별 최단경로를 추가해준다.
    for s in sources:
        if distance[s] != INF:
            answer.append(distance[s])
        # 경로가 없다면 -1 추가
        else:
            answer.append(-1)
    
    
    return answer

"""
    review: 다익스트라 알고리즘 문제라고 생각했다. 처음에 출발지별로 다익스트라를 전부 돌렸는데 시간초과가 났다. .. 당연하다 사실상 목적지가 전부 동일하기 때문에 목적지로부터 다익스트라를 수행하면 한번만 다익스트라 알고리즘을 수행해서 원하는 결과를 얻을 수 있다. 이렇게 변경하니 바로 문제가 풀렸다. 이제 다익스트라 알고리즘은 좀 익숙해진 것 같다...!!!!!
"""