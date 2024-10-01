from heapq import *

def solution(scoville, K):
    
    heapify(scoville) #최소힙으로 변경(기본이 최소힙, 오름차순)
    answer = 0
    mix = 0
    
    # 두개의 팝이 필요하니까 길이가 2이상일 때만 반복, 오름차순 정렬이니까 가장 작은 값이 K 이상이면 모든 음식의 스코빌 지수가 K이상이니 종료
    while len(scoville) > 1 and scoville[0] < K:
        minValue = heappop(scoville)
        maxValue = heappop(scoville)
        mix += 1
        scov = minValue + maxValue*2
        heappush(scoville, scov)
    
    # 전 부 섞음에도 불구하고 최소값이 K보다 작다면 -1리턴
    if scoville[0] < K:
        answer = -1
    # 섞은 횟수 출력
    else:
        answer = mix
    
        
    return answer