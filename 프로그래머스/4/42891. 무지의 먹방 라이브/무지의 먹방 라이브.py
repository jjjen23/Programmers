import heapq

def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1
                                                                                                                                     
    q = []
    
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    # 먹기위해사용한시간
    sum_val = 0
    # 직전에 다 먹은 음식 시간
    prev = 0
    
    length = len(food_times) #남은 음식의 개수
    
    while sum_val + ((q[0][0]-prev) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now - prev)*length
        length -=1
        prev = now
    
    res = sorted(q,key = lambda x : x[1]) # 키 순서로 정렬
    
    return res[(k-sum_val)%length][1]
    
    
    return answer















# 1번 음식부터 먹기 시작, 회전판은 번호가 증가하는 순서대로 음식을 무지앞으로 가져다 놓는다.
# 마지막 번호 -> 다시 1번 음식이 무지 앞으로 온다
# 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식 섭취 (아직 남은 음식 중 다음으로 가까운 번호의미)
# 먹방을 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
# 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지 알고자 한다.

# food_times: 각 음식을 모두 먹는데 필요한 시간이 담긴 배열
# 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇번 음식부터 다시 섭취하면 되는지 반환하라
# 만약 더 섭취해야 할 음식이 없다면 -1 반환

# 최소힙으로 해결
# import heapq

# def solution(food_times, k):
#     answer = 0
#     if sum(food_times) <= k:
#         return -1
#     q = []
    
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i],i+1))
    

#     length = len(food_times) # 남은 음식 개수
#     sum_value = 0 # 먹기 위해 사용한 시간
#     previous = 0 # 진전에 다 먹은 음식 시간
    
#     while sum_value + ((q[0][0] - previous)*length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now-previous) * length
#         length -= 1
#         previous = now
    
#     res = sorted(q, key = lambda x : x[1])

    
        
        
#     return res[(k-sum_value)%length][1]


"""
# 논리는 맞으나 시간 초과, 효율성 문제
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    answer = 0
    i = 0
    n = len(food_times)
    
    while k > -1:
        
        if food_times[i%n] != 0:
            food_times[i%n] -= 1
            answer = i%n
            # print(answer)
            i += 1
            k -= 1
        else:
            i += 1
            continue
    
    # answer += 1 
    
    return answer + 1
    
"""