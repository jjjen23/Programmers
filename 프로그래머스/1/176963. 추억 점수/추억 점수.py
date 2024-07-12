def solution(name, yearning, photo):
    answer = []
    
    # 이름-점수 사전 생성하기
    scoreDict = {}
    for i in range(len(name)):
        scoreDict[name[i]] = yearning[i]
    
    for a_photp in photo:
        tem_score = 0
        for name in a_photp:
            # 만일 사진에 그리운 인물이 등장한다면 그 인물의 점수를 더해준다.
            if name in scoreDict:
                tem_score += scoreDict[name]
        answer.append(tem_score)
        
    return answer