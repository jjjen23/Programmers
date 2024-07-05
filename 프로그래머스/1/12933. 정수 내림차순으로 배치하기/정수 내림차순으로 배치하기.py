def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    n = "".join(map(str,n))
    answer = int(n)
    
    return answer
