def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        tem = t[i:i+len(p)]
        
        # p보다 작거나 같은 수 카운트!
        if int(tem)<=int(p):
            answer += 1
            
    return answer
