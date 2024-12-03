import heapq
# 기본값인 최소힙을 활용해 최소 경로 탐색
def solution(N, road, K):
    INF = int(1e9) # 10억으로 설정
    
    # 노드 개수 : N개
    answer = 0
    graph =[[] for i in range(N+1)]
    distance = [INF] * (N+1)
    
    # 간선정보 입력받기(양방향 그래프)
    for R in road:
        a,b,c = R
        # a번 노드에서 b로 가는 비용이 c라는 의미
        graph[a].append((b,c))
        graph[b].append((a,c))
    # print(graph)

    
    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q,(0,start))
        distance[start] = 0
        
        while q:
            # 가장 짧은 노드 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 이미 처리된 노드라면 pass
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
    # 1번 마을에서 모든 마을까지 걸리는 최단 거리 정보
    dijkstra(1)
    for i in range(1,N+1):
        if K >= distance[i]:
            answer+=1
    # print(distance)
    
    return answer