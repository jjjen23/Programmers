# 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각 반환
# 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다.
# 9:00 ~ 23:59 : 버스 운영시각
# 00:01 ~ 23:59 : 버스 대기시각

# 버스는 9:00에 시작
# m: 한번에 탑승 가능한 승객
# t: 버스 배차 간격
# n: 운행버스

# 핵심은 마지막 버스..
# 마지막 출발버스가 여유있을때 -> 그 버스 탑승(마지막버스 출발시각에)
# 여유가 없다면 -> 초과하는 인원만큼 n분 빨리 탑승
def solution(n, t, m, timetable):
    answer = ''
    now = 9*60
    end = 23*60 + 59
    
    
    for i in range(len(timetable)):
        H,M = timetable[i].split(':')
        timetable[i] = int(H) * 60 + int(M)
    
    timetable.sort() # 오름차순정렬
    
    # 종료조건 : 운행 수
    while n > 0:
        n -= 1
        cnt = 0
        
        while timetable and timetable[0] <= now and cnt < m:
            last = timetable.pop(0)
            cnt += 1
        
        if n == 0: # 마지막 버스일 때
            if cnt < m :
                # 자리가 남았다면 출발시각에 도착
                answer = now
            else:
                # 자리가 없다면 마지막 탄 사람보다 1분 일찍 도착
                answer = last - 1
        else:
            now += t
        
                
                
    # print(now)
    # print(timetable)
    
    # 시간형식 변환
    answer = f"{answer//60:02d}:{answer%60:02d}"
    
    return answer