# if 늑대수 >= 양의수 : 모든 양 냠냠
# 늑대에게 양이 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모은 경우 리턴
# 음..일단 bfs일것 같고..dp도 써야 할 것 같아...
# 답지 참고

def solution(info, edges):
    answer = 0
    
    # 양이 늑대보다 많으면 양의 수를 결과 배열에 저장해둔다.(양이 늑대보다 같거나 적으면 해당 과정을 끝낸다.)
    
    # 방문된 부모노드와 방문되지 않은 자식 노드 정보가 있으면 1. 자식노드 방문처리 2. 양 or 늑대수 업데이트 
    
    visited = [0] * len(info)
    res = []
    
    # dfs로 모든 경우의 수 탐색
    def dfs(sheep, wolf):
        # 양이 늑대보다 많을때는 항상 기록!
        if sheep > wolf:
            res.append(sheep)
        # 종료조건: 양 <= 늑대
        else:
            return
        
        # 이진트리를 탐색하며 방문가능 노드를 찾는거야
        
        for p,c in edges:
            #방문가능한 노드: 부모 방문o,자식방문x인 노드
            
            if visited[p] and not visited[c]:
                visited[c] = 1
                # 자식노드가 양이라면 양추가해서 재귀
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                # 자식노드가 늑대라면 늑대 추가해서 재귀
                else:
                    dfs(sheep, wolf+1)
                    
                visited[c] = 0 # 백트래킹
                
    # 루트부터 시작
    visited[0] = 1 #루트 방문처리
    dfs(1,0) # 루트노드는 항상 양으로 시작한다!
    
    answer = max(res)
    # print(res)
    
    return answer

"""
    review: 내가 어려워하는 재귀문제이다. dfs와 백트레킹을 이용하는 문제..!!!!! 정답 이해도 겨우 했다. 탐색시 핵심 조건은 >>>자식노드로만 뻗어나가는게 아니라,방문했던 부모를 거쳐 다른 자식노드로도 갈 수 있다는 것<<< 같다.. 애초에 이 부분이 한번에 이해가 안돼서 더 생각하기 어려웠던 것 같다.
"""