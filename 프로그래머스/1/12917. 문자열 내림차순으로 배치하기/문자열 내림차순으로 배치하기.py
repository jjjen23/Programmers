def solution(s):
    s = list(s)
    s.sort(reverse=True)
    answer = "".join(map(str,s)) # 내림차순 정렬
    return answer