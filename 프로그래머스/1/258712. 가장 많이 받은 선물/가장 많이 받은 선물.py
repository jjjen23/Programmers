from itertools import combinations

def solution(friends, gifts):
    answer = 0
    
    # 정답 딕셔너리 생성(다음 달 받을 선물 수 저장)
    answerdict = {}
    
    # 총 저장 딕셔너리 생성
    total = {}
    
    # 선물 지수 딕셔너리 생성 
    giftgisu = {}
    
    setfriends = set(friends)
    for name in friends:
        answerdict[name] = 0
        meexcludelist = list(setfriends - {name})
        total[name] = {i : 0 for i in meexcludelist}
        
    #print(total)
    
    for gift in gifts:
        send, receive = gift.split(" ")
        total[send][receive] += 1
    
    print(total)
    
    # 선물지수 계산 렛츠고!
    for name in friends:
        sendgift = sum(total[name].values())
        receivegift = 0
        #meexcludelist = list(setfriends - {name})
        
        for i in total[name].keys():
            receivegift += total[i][name]
        
        # 사람 별 선물지수 저장
        giftgisu[name] =  sendgift - receivegift
    
    print(giftgisu)
    
    # 중복 계산 되는 부분을 해결해야함.. +_+ -> 기존 모든 조합에서 조합 함수 이용. 
    for comb in combinations(friends,2):
        name, who = comb[0], comb[1]
        if total[name][who] > total[who][name] :
            answerdict[name] += 1 
        elif total[name][who] < total[who][name] :
            answerdict[who] += 1

        # 두 사람이 주고 받은 선물의 수가 같거나, 없을 때
        else:
            if giftgisu[name] > giftgisu[who]:
                answerdict[name] += 1
            elif giftgisu[name] < giftgisu[who]:
                answerdict[who] += 1
                    
    print(max(answerdict.values()))
    answer = max(answerdict.values())
    
    return answer


"""
# 정답 : 1.  (중복 계산되는 형태로 2로 나눠줌.)
def solution(friends, gifts):
    answer = 0
    
    # 정답 딕셔너리 생성(다음 달 받을 선물 수 저장)
    answerdict = {}
    
    # 총 저장 딕셔너리 생성
    total = {}
    
    # 선물 지수 딕셔너리 생성 
    giftgisu = {}
    
    setfriends = set(friends)
    for name in friends:
        answerdict[name] = 0
        meexcludelist = list(setfriends - {name})
        total[name] = {i : 0 for i in meexcludelist}
        
    #print(total)
    
    for gift in gifts:
        send, receive = gift.split(" ")
        total[send][receive] += 1
    
    print(total)
    
    # 선물지수 계산 렛츠고!
    for name in friends:
        sendgift = sum(total[name].values())
        receivegift = 0
        meexcludelist = list(setfriends - {name})
        
        for i in meexcludelist:
            receivegift += total[i][name]
        
        # 사람 별 선물지수 저장
        giftgisu[name] =  sendgift - receivegift
    
    print(giftgisu)
    
    # 중복 계산 되는 부분을 해결해야함.. +_+
    for name in friends: 
        for who in total[name].keys():
            if total[name][who] > total[who][name] :
                answerdict[name] += 1 
            elif total[name][who] < total[who][name] :
                answerdict[who] += 1
            
            # 두 사람이 주고 받은 선물의 수가 같거나, 없을 때
            else:
                if giftgisu[name] > giftgisu[who]:
                    answerdict[name] += 1
                elif giftgisu[name] < giftgisu[who]:
                    answerdict[who] += 1
                    
    print(max(answerdict.values()) // 2)
    answer = max(answerdict.values()) // 2
    
    return answer
"""