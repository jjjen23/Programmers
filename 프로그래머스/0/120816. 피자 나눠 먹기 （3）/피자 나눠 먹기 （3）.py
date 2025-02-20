from math import ceil

def solution(slice, n):
    
    # 무조건 올림
    answer = ceil(n/slice)
    
    return answer