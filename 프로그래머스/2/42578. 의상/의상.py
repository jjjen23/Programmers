from itertools import combinations

def solution(clothes):
    answer = 0
    fashion  = {}
    for cloth in clothes:
        if cloth[1] not in fashion:
            fashion[cloth[1]] = 1
        else:
            fashion[cloth[1]] += 1
            
    # print(fashion)
    # catelist = list(fashion)
    # print(catelist)
    
    # 하나씩 착용하는 경우의 수
    # answer += sum(fashion.values())
    
    # # 조합해서 착용하는 경우의 수
    # for i in (2,len(fashion)+1):
    #     #print(i)
    #     for tuple in combinations(catelist,i):
    #         #print(tuple)
    #         tem = 1
    #         for j in tuple:
    #             tem *= fashion[j]
    #         answer += tem        
    # # print(sum(fashion.values())) # 총 옷들의 수
    # # print(len(fashion)) # 옷 카테고리는 몇개인지
    
    
    # 하나씩 착용하는 경우의 수
    #answer += sum(fashion.values())
    #print(answer)
    
    # 조합해서 입는 경우의 수
    if len(fashion) > 1:
        tem = 1
        for cnt in fashion.values():
            tem *= (cnt + 1)

        answer += (tem - 1)
        #print(answer)
        
    # 옷 카테고리가 하나인 경우
    else: 
        answer += sum(fashion.values())
    
    return answer