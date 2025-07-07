def solution(num_list, n):
    answer = []
    
    # 0 1 , 1,2, 3,4
    for i in range(0,len(num_list)-n+1,n):
        answer.append(num_list[i:i+n])
    return answer