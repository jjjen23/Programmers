def solution(s):
    #answer = True
    
    stack = [s[0]]
    
    for i in range(1,len(s)):
        stack.append(s[i])
        
        #print(stack)
        
        if len(stack)>=2:
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()
        
        #print(stack)
    
    if len(stack) != 0:
        answer = False
    else:
        answer = True
        
    return answer