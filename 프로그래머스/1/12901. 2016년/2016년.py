import calendar

def solution(a, b):
    # 0은 월요일
    yoil = calendar.weekday(2016,a,b)
    yoil_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    answer = yoil_list[yoil]
    return answer