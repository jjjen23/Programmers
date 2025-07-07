def solution(my_string):
    answer = 0
    temList = []
    # 문자열에 자연수가 없는 경우 0을 리턴
    tem = ''
    for s in my_string:

        if s.isdigit():
            tem += s
        else:
            if tem != '':
                temList.append(int(tem))
                tem = ''
                
    if tem != '':
        temList.append(int(tem))
    
    answer = sum(temList)
            
    
    return answer