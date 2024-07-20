def solution(s):
    s = list(s)
    answer = 0
    
    # 더이상 first와 비교될 대상이 없으면 종료하는 조건을 추가하기..!
    while len(s) > 0:
        first = s.pop(0)
        first_res = 1
        nexxt_res = 0
        tem_res = [first]
        
        while first_res != nexxt_res:
            if len(s) == 0:
                break
            
            nexxt = s.pop(0)
            tem_res.append(nexxt)
            if first != nexxt:
                nexxt_res+=1
            elif first == nexxt:
                first_res+=1
        print(tem_res)
        answer += 1
        
    return answer