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