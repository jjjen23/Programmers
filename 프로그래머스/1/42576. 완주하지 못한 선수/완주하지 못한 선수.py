# def solution(participant, completion):
    
#     participant.sort()
#     completion.sort()
    
#     for ant in completion:
#         if ant in participant:
#             participant.remove(ant)
            
#     answer = ''.join(map(str,participant))
    
#     return answer

def solution(participant, completion):
    participant_dict = {}
    
    # 참가자 목록을 딕셔너리에 추가
    for person in participant:
        if person in participant_dict:
            participant_dict[person] += 1
        else:
            participant_dict[person] = 1
    
    # 완주자 목록을 딕셔너리에서 제거
    for person in completion:
        if person in participant_dict:
            participant_dict[person] -= 1
    
    # 남은 참가자 찾기
    for person, count in participant_dict.items():
        if count > 0:
            return person