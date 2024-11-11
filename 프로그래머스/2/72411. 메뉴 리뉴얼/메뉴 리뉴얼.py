from itertools import combinations

def solution(orders, course):
    # 리스트 내 오름차순, 요소내부 오름차순 출력
    answer = []
    
    for cnt in course:
        ordercomdict = {}
        
        for order in orders:
            
            for ordercom in combinations(list(order),cnt):
                # 튜플형태 -> string으로 변환, 애초에 문자열을 정렬해서 저장
                sortedstring = ''.join(sorted(ordercom))
                
                # 딕셔너리에 조합이 이미 있다면 카운트 
                if sortedstring in ordercomdict:
                    ordercomdict[sortedstring] += 1
                # 딕셔너리에 없다면 생성
                else:
                    ordercomdict[sortedstring] = 1
        
        
        for k,v in ordercomdict.items():
            # 카운드 횟수가 동일하면 하나 이상도 추가됨
            if v >1 and v == max(ordercomdict.values()):
                answer.append(k)
    #최종 정렬
    answer.sort()
            
    
    return answer