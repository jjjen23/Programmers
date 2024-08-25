def solution(k, tangerine):
    answer = 0
    dict1 = {}
    settangerine = set(tangerine)
    
    for i in settangerine:
        dict1[i] = 0
    
    for i in tangerine:
        dict1[i] += 1
    
    dict1 = sorted(dict1.values(), reverse=True)
    # print(dict1)
    
    for i in range(len(dict1)):
        if k - dict1[i] > 0:
            answer += 1
            k -= dict1[i]
        else:
            answer += 1
            break
        
    return answer