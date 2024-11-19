def solution(diffs, times, limit):
    answer = []
    # 틀리면(diff - level) : time_prev+time_cur
    # 안틀리면, 다 틀린 이후 : time_cur
    # 제한 시간 내에 해결하기 위한 숙련도(level)의 최솟값
    left,right = min(diffs), max(diffs)
    
    while left <= right:
        sum = 0
        level = (left+right)//2
        sum += times[0]
        for i in range(1,len(times)):
            if level < diffs[i]:
                sum += (times[i-1]+times[i])*(diffs[i]-level)+times[i]
            else:
                sum+= times[i]
                
        if sum > limit :
            # right = level-1
            left = level + 1
        else:
            answer.append(level)
            right = level-1
            
    return answer[-1]