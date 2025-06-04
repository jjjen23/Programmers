def solution(my_string):
    answer = []
    idx = len(my_string)
    my_string = my_string[::-1]
    for i in range(1,idx+1):
        answer.append(my_string[:i][::-1])
    
    answer = sorted(answer)
        
    
    
    return answer