# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a # 일반적으로 작은 노드 번호가 부모
    else:
        parent[a] = b

def solution(n, costs):
    parent = [0] * (n+1)
    
    edges = []
    answer = 0
    
    
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, n+1):
        parent[i] = i
    
    for cost in costs:
        a, b, c = cost
        edges.append((c, a, b))
    
    # 간선을 비용순으로 정렬
    edges.sort()
    
    for edge in edges:
        c, a, b = edge
        
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent,a,b)
            answer += c

    
    return answer



"""
review: 다익스트라 알고리즘 이용하면 최소 간선 비용 나오겠다!!! 하고 다익스트라로 짰는데 다익스트라는 출발점에서 모든 노드까지 최단 거리를 구하는 알고리즘이었다.. >>모든 노드를 연결하는 최소 비용<< 을 구하는 최소신장트리 알고리즘은 대표적으로 1. 크루스칼 알고리즘과 2. 프림 알고리즘이 있다. 그 중 크루스칼 알고리즘을 참고하여 코드를 작성했다.

기본 크루스칼 알고리즘 코드랑 똑같은 수준의 문제이니까 알고리즘만 잘 숙지했다면 간단하게 풀었을듯 .. 다익스트라는 외웠는데 크루스칼은 안외웠다. ... 외워야겠다..

참고로 크루스칼 알고리즘은 그리디가 맞다. 

"""