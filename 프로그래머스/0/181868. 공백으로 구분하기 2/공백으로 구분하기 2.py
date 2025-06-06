def solution(my_string):
    answer = []
    tem = my_string.split(" ")
    print(tem)
    
    for i in tem:
        if len(i) > 0:
            answer.append(i)
            
    return answer