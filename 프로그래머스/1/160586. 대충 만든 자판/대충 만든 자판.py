def solution(keymap, targets):
    answer = []
    
    dict = {}
    
    # 각 알파벳 마다 최소 키 누룸 횟수를 딕셔너리 형태로 저장한다.
    for key in keymap:
        for i in range(len(key)):
            # 해당 알파벳이 딕셔너리에 없다면 생성하고 최소 키 횟수 저장
            if key[i] not in dict:
                dict[key[i]] = i+1
            # 만일 해당 알파벳이 딕셔너리에 있다면, 최소 키 횟수로 갱신하기
            if key[i] in dict:
                if i+1 <  dict[key[i]]:
                    dict[key[i]] = i+1
    
    #print(dict)
    
    # 타겟을 순회하며 최소 횟수 더해주기
    for target in targets:
        tem = 0
        for i in target:
            if i in dict:
                tem += dict[i]
            # 없는 알파벳인 경우 -1 을 저장하고, break문으로 탈출
            else:
                tem = -1
                break
        answer.append(tem)
    
            
    
    return answer