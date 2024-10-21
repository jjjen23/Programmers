def solution(skill, skill_trees):
    answer = 0
    
    #[CBD, CB, CD, C,]
    
    # 기존 순서 인덱스 추출해두기
    dict1 ={}
    for i in range(len(skill)):
        dict1[skill[i]] = i
    
    temlist = []
    for sk in skill_trees:
        tem = [] 
        for i in sk:
            if i in dict1:
                # 인덱스 값 추가
                tem.append(dict1[i])
        temlist.append(tem)
    
    #tem리스트 길이까지 0부터 순차적으로 구성되어있는지
    for tem in temlist:
        flag = True
        for i in range(len(tem)):
            if i != tem[i]:
                flag = False
        if flag == True:
            answer += 1
                
                
            
    return answer
