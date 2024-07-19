def solution(dartResult):
    n = ''
    score = []
    anwser = 0
    
    # 숫자를 모아.
    # 보너스 문자를 만나면 점수를 계산해. score 리스트에 추가해
    # 옵션 문자를 만나면, 2배를 해주거나, -1배를 해주면돼. 
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i =='T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
    
    answer = sum(score)
    
    return answer