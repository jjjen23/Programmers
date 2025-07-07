def solution(s):
    answer = ''
    
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    tem = []
    
    for k,v in dict1.items():
        if v == 1:
            tem.append(k)
            
    tem.sort()
    # print(tem)
    
    answer = ''.join(tem)
    
    
    return answer