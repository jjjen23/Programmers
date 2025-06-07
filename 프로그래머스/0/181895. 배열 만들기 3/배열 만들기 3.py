def solution(arr, intervals):
    answer = []
    for interval in intervals:
        s,e = interval[0], interval[1]

        answer.extend(arr[s:e+1])
        
    return answer