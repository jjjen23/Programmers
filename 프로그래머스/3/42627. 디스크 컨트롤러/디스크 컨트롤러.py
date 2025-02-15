import heapq

# 작업번호, 요청시간, 소요시간 저장
# 우선순위: 소요시간 짧은것 >요청 시간 빠른 것 > 작업 번호가 작은 것
# 모든 요청 작업의 반환 시간의 평균 정수 출력

def solution(jobs):
    answer = 0
    
    now = 0 # 현재시간
    idx = 0
    start = -1 #마지막 완료시간
    heap = []
    
    # 모든 작업 처리시까지 반복
    while idx < len(jobs):
        for job in jobs:
            # 이전작업 시작시간~종료시간 사이에 있던 작업요청들 힙에 넣기
            if start < job[0] <= now :
                # 우선순위 따라 역순으로 힙에 넣기
                heapq.heappush(heap, [job[1],job[0]])
        if heap:
            curr = heapq.heappop(heap)
            # 이전 작업 시작시간
            start = now
            # 이전 작업 종료시간이자 현재 시간
            now += curr[0]
            # 처리시간 누적(현재 - 요청시각)
            answer += (now - curr[1])
            idx += 1 # 처리된 거 카운트
        # 처리할 작업이 없다면, 현재 시각 범위를 1초씩 늘려서 작업 재탐색한다!
        else:
            now += 1
                
    
            
    # 1. 요청시간이 이전 작업 종료시간보다 작거나 같다면 힙에 삽입 
    # 2. 힙길이가 0일 때 까지 반환시간 계산해서 누적
    # jobs 길이가 끝날때 까지 1,2반복
    # 누적 반환시간 // len(jobs)가 정답
    
    answer = answer // len(jobs)
        
    return answer

"""
    review: 수도코드는 잘짰지만 구현을 못한 슬픈 사례.
    
"""