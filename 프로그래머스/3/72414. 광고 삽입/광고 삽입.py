# 시청자들이 가장 많이 보는 구간에 공익광고 넣기
# 최대 교집합 구간구하기 -> 해당 구간 시청자 누적 재생 시간 구하기(재생시간 합)
# 공익 광고가 들어갈 시작 시간을 구해서 반환, 만일 누적 재생 시간이 가장 많은 곳이 여러 곳 -> 가장 빠른 시작 시각 반환
# 초단위 int 형식으로 변환
def str_to_int(time):
    hh,mm,ss = time.split(":")
    return int(hh)*3600 + int(mm) * 60 + int(ss)

# int를 다시 원래 형식으로 변환
def int_to_str(time):
    h = time//3600
    time %= 3600
    m = time // 60
    time %= 60
    s = time
    
    return f"{h:02d}:{m:02d}:{s:02d}"


def solution(play_time, adv_time, logs):
    answer = ''
    
    # if play_time == adv_time:
    #     return '00:00:00'
    
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    # 초 구간별 시청자 수 누적 기록할 배열 생성
    all_time = [0 for i in range(play_time + 1)]
    
    for time in logs:
        start, end = time.split("-")
        start = str_to_int(start)
        end = str_to_int(end)
        # 시작 점에 +1
        all_time[start] += 1
        # 종료 지점에서 -1
        all_time[end] -= 1
    
    # 구간 별 중간값을 만드는 과정 , 구간 별 시청자수 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
    
    # 구간별 중간값을 채웠으니, 전체 누적 재생시간 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i-1]
        
    # 가장 누적 재생시간이 많은 곳 찾기
    # 광고 시작점 = end구간 - adv_time
    most_view = 0
    max_time = 0
    
    # 그냥 광고길이 == 동영상 길이면 00:00:00출력하면 ㅇ안돼? --> 네 안됨. 근데 왜지? 뭐가다른거지 ㅜ?
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i-adv_time]:
                most_view = all_time[i] - all_time[i-adv_time]
                max_time = i-adv_time+1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]  
                max_time = i - adv_time + 1   # 00:00:00
            
    answer = int_to_str(max_time)
    
    
    return answer


"""
    review: 누적합을 응용하는 방법을 참고했다.(답지 참고)
    누적합을 이렇게 쓸 수 구나.. 감탄. 
"""