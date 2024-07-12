def solution(cards1, cards2, goal):
    #answer = ''
    
    for word in goal:
        
        #빈 리스트가 아닌지 검사해야 인덱스오류안남!
        if len(cards1) > 0 and word == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and word == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"