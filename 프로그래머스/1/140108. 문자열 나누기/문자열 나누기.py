def solution(s):
    s = list(s)
    answer = 0
    
    # 문자열이 없을 때 까지 반복
    while len(s) > 0:
        first = s.pop(0)
        first_res = 1
        nexxt_res = 0
        tem_res = [first]
        
        # 첫글자 카운트 수와 첫글자 제외 카운트 수가 동일할 때 까지 반복
        while first_res != nexxt_res:
            # 더 이상 읽을 문자열이 없다면, 지금까지 읽은 문자열 분리 후, 종료
            if len(s) == 0:
                break
            
            nexxt = s.pop(0)
            tem_res.append(nexxt)
            if first != nexxt:
                nexxt_res+=1
            elif first == nexxt:
                first_res+=1
        print(tem_res)
        # 두번째 while문 종료 -> 문자열 분리됨 의미, 정답에 1씩 더하기 
        answer += 1
        
    return answer