import math

def solution(progresses, speeds):
    answer = []
    nameunday = []
    
    # 작업이 끝나기 까지 남은 일 수 계산해주기
    for i in range(len(progresses)):
        tem = math.ceil((100 - progresses[i]) / speeds[i])
        nameunday.append(tem)
    
    #print(nameunday)
    
    # 리스트가 비어 있지 않을 때까지 반복
    while len(nameunday):
        m = nameunday.pop(0)
        tem = 1
        
        # 리스트가 비어있지 않고, 뒷순서가 나보다 작다면 오늘 릴리즈할 기능수 증가시켜주기
        while nameunday and m >= nameunday[0]:
            nameunday.pop(0)
            tem += 1
        
        # 뒷순서가 크다면 정답에 추가 -> 다시 반복
        answer.append(tem)
    
        
    return answer