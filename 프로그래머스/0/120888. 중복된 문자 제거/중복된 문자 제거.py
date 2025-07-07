def solution(my_string):
    answer = ''
    # 공백도 하나의 문자로 구분
    # 중복된 문자 중 가장 앞에 있는 문제를 남김
    
    check = []
    for i in my_string:
        if i not in check:
            check.append(i)
            answer += i
        else:
            continue
    
    return answer