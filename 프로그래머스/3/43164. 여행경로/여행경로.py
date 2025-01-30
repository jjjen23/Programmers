from collections import deque

def solution(tickets):
    answer = []
    


    graph = {}
    
    for ticket in tickets:
        start, end = ticket
        
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
            
        graph[start].sort(reverse=True) # 역순으로 정리 pop()으로 해야 시간 효율이 좋으므로...
            
    # 인천에서 시작
    stack = ["ICN"]
    
    while stack:
        tem = stack [-1]
        
        if tem not in graph or len(graph[tem]) == 0:
            answer.append(stack.pop())
            # print(answer)
        else:
            stack.append(graph[tem].pop())
            # print(stack)
    
    
        # [icn] = [sfo, atl]
        # [sfo] = [atl]
        # [atl] = [sfo]

    
    
    print(answer)
    
    
    return answer[::-1]