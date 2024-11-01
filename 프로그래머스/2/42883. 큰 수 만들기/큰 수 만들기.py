def solution(number, k):
    answer = ''
    #k개의 수를 제거했을때 순열로 만들 수 있는 가장 큰 수
    # 순서를 유지하며 가장 큰 수를 하나씩 넣는다!!!!
    # 가장 큰 수를 찾았을때 그 수 앞은 다 날려야함.
    # 조건 1 : 큰 수를 찾았을 때 그 앞을 다 날린다.
    # 조건 2 : 뒤에 k-현재 확정수 만큼의 수가 있어햐 한다.
    # 그리디...........
    
    stack = []
    
    for num in number:
        while k > 0 :
            # 스택에 값이 있을 때 그리고 스택 마지막 값이 현재 num보다 작다면 pop
            if stack and stack[-1] < num:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)
    # print(stack)
        
                
    answer = ''.join(stack[:len(stack)-k])
        
    
    
    return answer