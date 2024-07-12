def solution(k, score):
    answer = []
    award_list = []
    for i in range(len(score)):
        if len(award_list) < k :
            award_list.append(score[i])
            answer.append(min(award_list))
        else:
            minValue = min(award_list)
            if  minValue < score[i] :
                indexNum = award_list.index(minValue)
                award_list[indexNum] = score[i]
                answer.append(min(award_list))
            else:
                answer.append(min(award_list))
        
    return answer