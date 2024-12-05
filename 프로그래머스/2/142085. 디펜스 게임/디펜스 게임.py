import heapq

def solution(n, k, enemy):
    # 무적권이 적보다 많으면 그냥 enemy길이 출력
    if k >= len(enemy):
        return len(enemy)
    
    priQueue = []
    
    for i in range(len(enemy)):
        heapq.heappush(priQueue,enemy[i])
        if len(priQueue) > k:
            # 젤 작은케 팝됨, 힙에는 가장 큰 수 k개가 남아있음
            last = heapq.heappop(priQueue)
            # n보다 적이 더 많다면 종료 -> 해당 라운드 반환
            if last > n:
                return i
            n -= last
    # 무적권 다쓰고 적을 모든 라운드에서 처리 가능 -> enemy길이
    return len(enemy)