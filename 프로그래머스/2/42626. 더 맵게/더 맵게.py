from heapq import *

def solution(scoville, K):
    
    heapify(scoville)
    answer = 0
    mix = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        minValue = heappop(scoville)
        maxValue = heappop(scoville)
        mix += 1
        scov = minValue + maxValue*2
        heappush(scoville, scov)
    
    if scoville[0] < K:
        answer = -1
    else:
        answer = mix
    
        
    return answer