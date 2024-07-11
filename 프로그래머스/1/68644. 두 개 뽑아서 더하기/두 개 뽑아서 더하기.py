def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    answer_set = set(answer)
    answer = list(answer_set)
    answer.sort()
            
    return answer