def solution(citations):
    citations.sort()
    
    # 최대값부터 0 까지 검사
    for i in range(citations[-1], -1, -1):
        h = i
        
        #조건1 
        # h편 이상 인용 된 논문의 수가 >= h
        upcnt = 0
        res=[]
        for k in citations:
            if k >= h:
                upcnt += 1
            else:
                res.append(k)
        
        #조건2
        # 조건 1에 해당하는 논문을 제외하고 나머지 논문의 인용 수가 <= h 
        dwonflag = True
        for k in res:
            if k > h:
                dwonflag = False
                break
        
        
        # 조건1, 2모두 만족하는 h 출력 후 종료 -> return h 하고 종료.
        if upcnt >= h and dwonflag == True:
            return h
        