def solution(s):
    answer = []
    
    list_s = s[2:-2].split("},{")
    
    list_2 = [] 
    for i in list_s:
        list_2.append(i.split(","))
    
    list_2 = sorted(list_2, key = lambda x : len(x))
    
    answer.append(int(list_2[0][0]))
    for i in range(1, len(list_2)): 
        answer.append(int(list(set(list_2[i])-set(list_2[i-1]))[0]))
        
    return answer