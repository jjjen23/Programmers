def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort() #길이가 0이 아니라면 오름차순 정렬

    return answer