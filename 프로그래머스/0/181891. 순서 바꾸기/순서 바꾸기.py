def solution(num_list, n):
    # n 번째 이후 원소들 + n 번째 까지 원소
    
    answer = num_list[n:] + num_list[:n]
    
    return answer