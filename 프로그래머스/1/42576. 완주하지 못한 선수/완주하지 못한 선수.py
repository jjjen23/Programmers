# def solution(participant, completion):
    
    # 시간초과 : 해당 코드 이용시 시간복잡도 O(n*m)
#     for ant in completion:
#         if ant in participant:
#             participant.remove(ant)
            
#     answer = ''.join(map(str,participant))
    
#     return answer

# 딕셔너리(해시맵)이용시 시간복잡도 O(n)
def solution(participant, completion):
    
    partDict = {}
    
    for i in participant:
        if i not in partDict:
            partDict[i] = 1
        # 동명이인의 경우 +1
        else:
            partDict[i] += 1
    
    # 완주선수 리스트에서 -1 해주기
    for i in completion:
        if i in partDict:
            partDict[i] -= 1
    
    for part, cnt in partDict.items():
        # 값이 0이 아닌 참가자가 완주하지 못한 참가자.(동명이인도 마찬가지) 
        if cnt != 0:
            answer = part
            
    return answer

