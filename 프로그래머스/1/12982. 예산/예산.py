def solution(d, budget):
    #오름차순 정렬
    d.sort()
    
    # 예산과 같거나 작을때까지 가장 왼쪽(큰것)부터 제거
    while sum(d) > budget:
        d.pop()
        
    
    answer = len(d)
    return answer