def solution(before, after):
    answer = 0
    
    # before과 after의 구성이 같으면 1 아니면 0
    
    dict1 = {}
    dict2 = {}
    
    for i in before:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    for i in after:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    
    if dict1 == dict2 :
        answer = 1
    else:
        answer = 0
    
    
    return answer