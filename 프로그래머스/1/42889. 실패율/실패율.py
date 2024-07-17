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
    
    items = sorted(answerDict.items(), key = lambda x : x[1], reverse=True)
    
    for item in items:
        answer.append(item[0])
        
    return answer