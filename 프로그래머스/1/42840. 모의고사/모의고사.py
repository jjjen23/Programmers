def solution(answers):
    supoza1 = [1,2,3,4,5]
    supoza2 = [2,1,2,3,2,4,2,5]
    supoza3 = [3,3,1,1,2,2,4,4,5,5]
    
    total1 = 0
    total2 = 0
    total3 = 0
    
    for i in range(len(answers)):
        if supoza1[i % len(supoza1)] == answers[i]:
            total1+=1
        if supoza2[i % len(supoza2)] == answers[i]:
            total2+=1
        if supoza3[i % len(supoza3)] == answers[i]:
            total3+=1
    
    # 딕셔너리에 각 수포자의 총 점수 저장
    res = {1:total1, 2:total2, 3:total3}
    
    # 가장 최고 점수를 저장해두기
    max_value = max(res.values())
    
    answer = []
    
    # 최고 점수와 동일한 점수를 가진 수포자 번호를 정답 리스트에 저장
    for item in res.items():
        if item[1] == max_value:
            answer.append(item[0])
    
    # 가장 높은 점수를 받은 사람이 여럿일 경우, 오름차순 정렬해주기
    answer.sort()
    
    
    return answer