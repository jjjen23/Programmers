def solution(N, stages):
    answer = []
    # 실패율을 구하는 코드를 완성하라
    # 스테이지에 도달 했지만 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    # 이용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
    # 스테이지 개수 N
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 반환하라
    dict1 = {}
    for i in range(1,N+1):
        dict1[i] = 0
    
    

    for i in range(1,N+1):
        # i 번 스테이지의 실패율을 구하자
        arrived = 0
        notclear = 0
        
        for s in stages:
            if s >= i :
                arrived += 1
            if i == s:
                notclear +=1 
        # print(arrived,notclear)
        if arrived == 0:
            dict1[i] = 0.0
        else:
            dict1[i] = notclear/arrived
    # print(tem)
    temdict = sorted(list(dict1.items()),key = lambda x : (-x[1],x[0]))
    for i in range(N):
        answer.append(temdict[i][0])
    
    # 실패율이 높은 스테이지 부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 반환하라(만일 실패율이 같다면 번호가 작은게 먼저)
    return answer













"""
def solution(N, stages):
    rates = []
    answer = []
    user = len(stages)
    
    
    for i in range(1,N+1):
        tem = stages.count(i)
        if tem == 0:
            rates.append(0)
        else:
            rates.append(tem/user)
            user -= tem
    
    answerDict = {}
    for i in range(len(rates)):
        answerDict[i+1] = rates[i]
    
    items = sorted(answerDict.items(), key = lambda x : -x[1])
    
    for item in items:
        answer.append(item[0])
        
    return answer


"""



