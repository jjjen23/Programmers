from itertools import combinations 

def solution(relation):
    answer = 0
    resList = []
    # 중복 x 
    # 묶어서 키가 되려면 최소성 만족 -> 하나짜리 후보키랑 비교해선 x
    # 집합으로 만들어서 추가했을 때 열의 길이랑 같다면 유일성 만족. 최소성 만족한다면 바로 추가 
    # 일단 하나짜리 후보키를 찾아 -> 찾았으면 그거 제외하고 최소 키를 찾아 -> 또 그거 제외하고 최소키를 찾아
    # 하나 짜리 후보키 못 찾았어 -> 범위 늘려서 후보키 찾아 -> 없으면 또 늘려..
    test = list(range(len(relation[0])))
    for i in range(1,len(relation[0])+1):
        for com in combinations(test,i):
            tem = {tuple(rel[idx] for idx in com) for rel in relation}
                    
            if len(tem) == len(relation):
                # 최소성 구하기 : 이미 추가된 조합과 새로 검증하는 조합이 서로의 부분집합히면 안됨!!!!!
                if not any(set(key).issubset(set(com)) for key in resList):
                    resList.append(com)
    answer = len(resList)



    
    return answer