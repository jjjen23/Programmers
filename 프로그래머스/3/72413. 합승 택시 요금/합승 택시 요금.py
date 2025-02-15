# 출발지점에서 a,b 두 지점까지 최저 거리 계산 단, 합승해서 비용이 짧아지는 구간에 대해선 합승한다.
# 다익스트라

# 시작지점에서 특정 노드까지 최소비용 + 특정 노드에서 a,b까지 최소비용 값이 가장 작은 것-> 최적 합승 비용
# 1. s에서 출발하는 다익스트라
# 2. a에서 출발하는 다익스트라
# 3. b에서 출발하는 다익스트라
# 1,2,3의 거리를 합쳐서 최소 합승 지점(M)을 찾는다.

# a->m까지 거리 + b->m까지 거리 + s->m까지 거리를 합산한게 정답이된다.
import heapq


def solution(n, s, a, b, fares):

    INF = int(1e9)
    
    s_distance = [INF] * (n+1)
    a_distance = [INF] * (n+1)
    b_distance = [INF] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    
    for fare in fares:
        x,y,z = fare
        graph[x].append((y,z))
        graph[y].append((x,z))
    
    def dijkstra(start,distance):
        q = []
        
        heapq.heappush(q,(0,start))
        distance[start] = 0
        
        while q:
            dist, now  = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
            
            for i in graph[now]:
                cost = dist+i[1]
                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost, i[0]))
                        
    dijkstra(s,s_distance)
    dijkstra(a,a_distance)
    dijkstra(b,b_distance)
    
    answer = INF
    point = -1 # 분기점 저장
    
    for i in range(1,len(s_distance)):
        sum = s_distance[i]+a_distance[i]+b_distance[i]
        if sum < answer:
            answer = sum
            point = i
            
    # print(answer)
    # print(point)
    
    
    
    return answer