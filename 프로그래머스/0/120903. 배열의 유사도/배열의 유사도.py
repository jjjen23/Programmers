def solution(s1, s2):
    answer = 0
    
    if len(s1) < len(s2):
        for s in s1:
            if s in s2:
                answer += 1
    else:
         for s in s2 :
                if s in s1:
                    answer += 1
    
    return answer