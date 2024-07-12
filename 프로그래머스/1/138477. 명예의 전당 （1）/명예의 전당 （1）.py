def solution(k, score):
    answer = []
    award_list = []
    for i in range(len(score)):
        
        if len(award_list) < k :
            award_list.append(score[i])
            answer.append(min(award_list))
        else:
            if  min(award_list) < score[i] :
                award_list.remove(min(award_list))
                award_list.append(score[i])
            
            answer.append(min(award_list))
        
    return answer