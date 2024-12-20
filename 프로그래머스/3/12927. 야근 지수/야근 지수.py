import heapq 

def solution(n, works):
    answer = 0
    
    # 남은 작업량이 없는 경우
    if sum(works) <= n:
        return 0
    # 남은 작업량이 있는 경우-> 남은 것들의 제곱이 최소가 되도록 조정할 것..
    # 최소힙으로 작동 음수로 바꿔 저장 시 가장 작은 값이 출력=양수일때 가장 큰 값
    works = [-i for i in works]
    heapq.heapify(works)
    
    # 매번 가장 큰값을 꺼내서 하나씩 빼주고 다시 넣으면 됨
    while n:
        n -= 1
        work = heapq.heappop(works)
        # print(work)
        work += 1
        heapq.heappush(works, work)
    
    for w in works:
        answer += w**2
    
    return answer