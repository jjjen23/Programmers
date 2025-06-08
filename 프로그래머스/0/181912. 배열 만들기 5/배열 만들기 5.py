def solution(intStrs, k, s, l):
    answer = []
    for Str in intStrs:
        # print(Str[s:s+l])
        if int(Str[s:s+l]) > k:
            answer.append(int(Str[s:s+l]))
    return answer