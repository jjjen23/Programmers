def solution(sizes):

    smalls=[] # 두 변 중에서 더 작은 작은 변의 길이를 몰아 넣은 리스트
    larges=[] # 큰 길이 몰아넣은 리스트
    
    for size in sizes:
             larges.append(max(size))
             smalls.append(min(size))
                
    # 정답 = 작은 것 중 큰 것 * 큰 것 중 큰 것
    answer = max(smalls) * max(larges)        
    
    return answer