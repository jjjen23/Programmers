def solution(bandage, health, attacks):
    answer = 0
    
    maxsec =  attacks[-1][0] + 1 
    
    
    attackssec = {}
    for attack in attacks:
        attackssec[attack[0]] = attack[1]
        
    
    
    max_health = health
    
    cnt_compensation = 0 # 연속공격 카운터
    compensationsec = bandage[0] # 연속공격
    secrecovery = bandage[1] # 초당 회복
    plusrecovery = bandage[2] # 연속 공격 성공시 보상 회복
    
    for i in range(maxsec): 
        print(health)
        # 공격이 있는 시간 이라면
        if i in attackssec:
            health -= attackssec[i]
            if health <= 0 :
                break
            cnt_compensation = 0    
            
        else:
            cnt_compensation += 1
            health += secrecovery
            health = min(max_health, health)
            
            if cnt_compensation == compensationsec:
                health += plusrecovery
                health = min(max_health, health)
                cnt_compensation = 0
            # else:
            #     health += secrecovery
            #     health = min(max_health, health)

    
    print(health)
    if health <= 0:
        answer = -1
    else:
        answer = health
        
    return answer