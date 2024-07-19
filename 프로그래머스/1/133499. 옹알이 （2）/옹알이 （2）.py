def solution(babbling):
    # 가능한 발음 리스트
    cando = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    # 같은 발음을 연속해서 불가능 -> 이걸 해결해야한다.. 
    # 안되는 반례 yewooye인 경우 ye만 남아버림..
    for word in babbling:
        for can in cando:
            # 중복된 단어가 없다면 can을 " "으로 변경하라
            if can * 2 not in word:
                word = word.replace(can, " ") 
                
        # 공백으로 이루어져있는지 검사한다.
        if word.isspace():
            answer += 1
            
    return answer