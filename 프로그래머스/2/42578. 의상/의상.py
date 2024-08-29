from itertools import combinations

def solution(clothes):
    answer = 0
    
    # 카테고리별 옷의 수 저장(옷의 종류는 상이하다.)
    fashion  = {}
    for cloth in clothes:
        if cloth[1] not in fashion:
            fashion[cloth[1]] = 1
        else:
            fashion[cloth[1]] += 1
    
    # 조합해서 입는 경우의 수 => a,b,c 조합으로 가능한 모든 경우의 수 : a*b*c
    if len(fashion) > 1:
        tem = 1
        for cnt in fashion.values():
            # 각각의 카테고리를 안입는 경우의 수 1 추가(ab,ac,bc 같은 경우에 해당)
            tem *= (cnt + 1)
        # 모든 카테코리를 안입는 경우의 수(공집합) 제외 시켜주기
        answer += (tem - 1)
        #print(answer)
        
    # 옷 카테고리가 하나인 경우
    else: 
        answer += sum(fashion.values())
    
    return answer