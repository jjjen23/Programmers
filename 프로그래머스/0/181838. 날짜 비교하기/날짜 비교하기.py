def solution(date1, date2):
    answer = False
    for i in range(len(date1)):
        if date1[i] == date2[i]:
            continue
        elif date1[i] < date2[i]:
            return 1
        else:
            return 0
    return 0