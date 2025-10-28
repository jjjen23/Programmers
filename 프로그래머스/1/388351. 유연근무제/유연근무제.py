def solution(schedules, timelogs, startday):
    answer = 0
    
    # 출근 희망 시각에 늦지 않고 출근한 직원들에게 상품을 줌
    # 출근 희망 시각 + 10분 까지 출근 가능 (단, 토,일 출근시각은 이벤트에 영향x)
    # 모든시각은 시에 100을 곱하고 분을 더한 정수로 일괄표현
    
    # answer : 직원이 설정한 출근 희망 시각과 실제 출근 기록을 바탕으로 상품을 받을 직원 수를 리턴
    # schedules : 출근 희망시각 배열
    # timelogs : 실제 출근 시각
    # startday : 이벤트를 시작한 요일을 의미하는 정수(1~7)
    
    
    
    n = len(schedules)
    
    for i in range(n):
        tem = schedules[i] + 10 
        if tem % 100  > 59:
            n10 = tem // 100 + 1
            n20 = tem % 100 - 60
            tem = n10*100 + n20
        schedules[i] = tem
    
    for i in range(n):
        settime = schedules[i]
        
        flag = True
        tem_startday = startday
        for realtime in timelogs[i]:    

                
            # 주말이 아니고 늦은 경우에는 상품못줘
            # 주말은 패스
            if tem_startday in [6,7]:
                # 날짜만 업데이트 하고 다음으로 이동
                tem_startday += 1
                if tem_startday > 7:
                    tem_startday = 1
                    
                continue
            else:
                if realtime > settime:
                    flag = False
                    break
                    
            tem_startday += 1
            if tem_startday > 7:
                tem_startday = 1
            
        if flag == True:
            answer += 1
    
    return answer