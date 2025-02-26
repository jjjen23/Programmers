# referral내에서 i번째에 있는 이름은 enroll내에서 i번째에 있는 판매원을 조직에 참여시킨 사람의 이름

# 칫솔하나당 100원

def solution(enroll, referral, seller, amount):
    
    res = {} # 결과 저장 딕셔너리
    for name in enroll:
        res[name] = 0
    
    parents = {}
    # enroll에 i요소보다 먼저 나온 요소들은 부모 상위관계가 확정되어 있음 -> 바로 상위 부모 관계들만 바로 하위에 extend해주면 됨
    # 부모관계 확립
    for i in range(len(enroll)):
        if enroll[i] not in parents:
            parents[enroll[i]] = [referral[i]]
        else:
            parents[enroll[i]].append(referral[i])
            
        parent = referral[i]
        # 부모가 있다면 바로 윗세대 부모 요소 추가
        if parent in parents:
            parents[enroll[i]].extend(parents[parent])

    # print(parents)
    
    for i in range(len(seller)):
        origin = amount[i] * 100 
        commission = int(origin * 0.1) 
        res[seller[i]] += (origin - commission)
        
        for who in parents[seller[i]]:
                origin = commission
                commission = int(origin * 0.1)
                if commission < 1 and who in res:
                    res[who] +=  (origin - commission)
                    break
                if who in res:
                    res[who] +=  (origin - commission)
    # print(res)

    
    # 하나빼고 다 맞다. 
            
    return list(res.values())