def solution(n, times):
    answer = 0
    
    # 모든 사람이 심사받는데 걸리는 최소 시간 반환
    Min = min(times)
    Max = n * max(times)
    
    # 모든사람을검사하는데 걸리는 총시간에 각 심사관의 심사시간을 나누면 total시간에 심사관당 몇명을 검사할 수 있는지 알 수 있다. -> 총 시간을 이진탐색으로 조정하면서 n명을 모두 검사할 수 있는 최소 시간을 찾는다!!!
    
    while Min <= Max:
        Mid = (Min + Max) // 2
        timepern = 0
        for i in times:
            timepern += Mid // i
        
        if timepern >= n:
            answer = Mid
            Max = Mid - 1
        else:
            Min = Mid + 1
    
    
    return answer


"""
def solution(n, times):
    answer = 0
    
    left = min(times) # 가능한 최소 시간
    right = max(times)*n # 인원수 만큼 가능한 최대
    
    # 임의의 시간 동안 몇 명이 심사 받을 수 있는지 확인 -> 값 최소로
    # 시간 최소, 최대 범위 구하고 중간 값이 n명을 심사 할 수 있는 시간인지 확인하며 이분탐색 진행
    # 중간 값 시간 동안 n명보다 적게 심사 가능 -> 중간값 기준 오른쪽으로 이동
    # ex) 임의의 시간 30분 동안 심사가능 인원 -> (30//7) + (30//10)
    
    while left <= right:
        mid = (left+right) // 2
        checked = 0
        
        
        # ex) 임의의 시간 30분 동안 심사가능 인원 -> (30//7) + (30//10)
        for time in times:
            checked += mid // time
            # 중간에 이미 n보다 같거나 크다면 탈출
            if checked >= n :
                break
        
        if checked >= n:
            answer = mid
            right = mid - 1
        elif checked < n :
            left = mid + 1
    
    return answer

"""