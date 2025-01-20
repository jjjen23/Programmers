def solution(n, s):
    answer = []
    
    # n > s : return -1
    if n > s :
        return [-1]
    else:
        while n > 0:
            tem = s // n
            answer.append(tem)
            s -= tem
            n -= 1
    
    return answer