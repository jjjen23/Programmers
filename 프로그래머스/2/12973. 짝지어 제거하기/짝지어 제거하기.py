def solution(s):
    answer = -1
    stack = [s[0]]
    
    
    for i in range(1,len(s)):
        tem = s[i]
        
        # 스택에 하나 이상의 요소가 있다면~
        if len(stack) > 0:
            if tem == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(tem)
                
        # 스택이 비어있다면 그냥 추가
        else:
            stack.append(tem)
            
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
        
        
    

    return answer