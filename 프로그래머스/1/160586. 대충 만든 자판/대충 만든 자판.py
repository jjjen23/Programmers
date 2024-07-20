def solution(keymap, targets):
    answer = []
    
    dict = {}
    
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dict:
                dict[key[i]] = i+1
            if key[i] in dict:
                if i+1 <  dict[key[i]]:
                    dict[key[i]] = i+1
    
    print(dict)
    
    for target in targets:
        tem = 0
        for i in target:
            if i in dict:
                tem += dict[i]
            else:
                tem = -1
                break
        answer.append(tem)
    
            
    
    return answer