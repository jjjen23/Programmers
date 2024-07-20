def solution(n, lost, reserve):
    answer = 0
    
    answer = n - len(lost) # 일단 체육복이 있는 사람
    
    
    # 여벌을 가져온 학생이 도난 당한 경우, 못빌려줘. 
    n = set(lost) & set(reserve) # 교집합.
    if len(n) != 0:
        for i in n:
            reserve.remove(i)
            lost.remove(i)
            answer += 1
    
    # 정렬 해야 정답됨.
    reserve.sort()
    lost.sort()
    
    # 둘 중 하나라도 만족하면 체육복있는 사람이 됨(단, 하나의 if문만 해당해야 함 -> 각 if문에 continue꼭 추가해야함)
    for i in lost:
        # 바로 앞번호에게 빌린 경우    
        if i-1 in reserve:
            answer+=1
            reserve.remove(i-1)
            continue
        
        # 바로 뒷번호에게 빌린 경우
        if i+1 in reserve:
            answer+=1
            reserve.remove(i+1)
            continue
            
    return answer