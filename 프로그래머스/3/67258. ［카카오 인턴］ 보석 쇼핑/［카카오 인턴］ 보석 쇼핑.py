# 문제 이해
# 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 구간 인덱스 번호+1 를 반환하라
# 만일 짧은 구간이 하나 이상 -> 시작 진열대 번호가 가장 작은 구간 반환!!
# 우선순위 1. 최소길이 2. 시작 인덱스가 작은 것 

def solution(gems):
    
    # 최악의 경우로 초기화 = 모든 요소 포함하는 경우
    best = [0,len(gems)]
    setgems = len(set(gems))
    
    gemdict = {}
    left , right = 0,0
    
    while right < len(gems):
        # 딕셔너리에 있다면 +1
        if gems[right] in gemdict:
            gemdict[gems[right]] += 1
        # 없다면 생성, 1로 초기화
        else:
            gemdict[gems[right]] = 1
        
        # 오른쪽 인덱스 이동
        right += 1
        
        # 모든 종류의 보석을 만족한다면 left를 이동하며 만족하는 최소 길이를 탐색
        while len(gemdict) == setgems:
            # 더 짧은 구간 인덱스로 갱신
            # 작을 때에 대해서만 갱신하므로 무조건 최소 인덱스로 갱신함(순차 탐색)
            if right - left < best[1] - best[0]:
                best = [left, right]
            
            # 포함하는 보석을 다 포함하고 있으면 왼쪽을 살살빼봐
            # 빼고도 len(gemdict) == setgems를 만족한다면 베스트 레인지 갱신!!!!
            gemdict[gems[left]] -= 1
            if gemdict[gems[left]] == 0:
                del gemdict[gems[left]]
            left += 1
        
        
    answer = [best[0]+1, best[1]]
    
    return answer


"""
review : 
1. 첫번째 방식 : 전수조사 -> 시간 초과

# 전수조사 -> 효율성 통과 안될 것 같아서 .. 일단 해봄
# 1. 모든 인덱스를 돌면서 i번째 인덱스를 기준으로 set에 있는 모든 요소가 들어왔다면 (첫번째 인덱스 기록, 구간길이 기록) 
# 2. 기록 된 것 중 구간 길이가 짧고, 첫번째 인덱스가 가장 작은것 출력 

def solution(gems):
    res = []
    answer = 0
    
    # 문제 이해
    # 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 구간 인덱스 번호+1 를 반환하라
    # 만일 짧은 구간이 하나 이상 -> 시작 진열대 번호가 가장 작은 구간 반환!!
    for i in range(0,len(gems)):
        setgems = set(gems)
        for j in range(i+1, len(gems)+1):
            # set에 있는 요소가 전부 있다면 기록하고 break
            if len(set(gems[i:j])) == len(setgems):
                res.append([i+1,j,j-i])
                break
                
    # print(res)
    # 구간 길이가 가장 짧은것 -> 첫 인덱스가 짧은 것 순으로 정렬
    res.sort(key = lambda x : (x[2],x[0]))
    # print(res[0])
    
    answer = res[0][:2]
    
    return answer


2. 딕셔너리, 투포인터 이용 -> set(gems[i:j]) 부분을 해결해야함: -> 구현 못해서 답지 참고, 투 포인터 사용이 익숙하지 않았고 딕셔너리를 이렇게 활용 할 생각은 못했다. 또한 최악의 경우로 초기화하는 방법도 생각 못함 항상 최악의 경우로 초기화해서 갱신하는 습관이 필요해보임!!

"""