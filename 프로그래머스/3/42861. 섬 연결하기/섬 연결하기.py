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