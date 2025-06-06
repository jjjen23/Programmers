def solution(myString):
    answer = []
    tem = myString.split('x')
    for i in tem:
        answer.append(len(i))
    return answer