def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        tem = 0
        for j in range(1,i+1):
            if i % j == 0:
                tem+=1
        if tem % 2 == 0:
            answer+=i
        else:
            answer-=j
    return answer