def solution(babbling):
    # 가능한 발음 리스트
    cando = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    # 같은 발음을 연속해서 불가능 -> 이걸 해결해야한다.. 
    # 안되는 반례 yewooye인 경우 ye만 남아버림..
    for i in range(len(babbling)):
        word = babbling[i]
        for can in cando:
            if can * 2 not in word:
                word = word.replace(can, " ") #첫번째 can만 ""로 변경
        babbling[i] = word
        print(babbling)
                
    for word in babbling:
        if word.isspace():
            answer += 1
            
    return answer