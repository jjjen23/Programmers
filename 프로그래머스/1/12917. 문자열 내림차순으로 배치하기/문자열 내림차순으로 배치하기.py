def solution(s):
    s = list(s)
    s.sort(reverse=True)
    answer = "".join(map(str,s))
    return answer