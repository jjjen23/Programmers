def solution(p):
    
    answer = ''
    
    if len(p) == 0:
        return ''
    
    # 괄호방향 뒤집는 함수
    def reverse(w):
        res = ''
        for i in w:
            if i == '(':
                res += ')'
            else:
                res += '('
        return res
    
    # 올바른 괄호 판별 함수
    def is_valid(u):
        if u[0] == ")":
            return False
        u = list(u)
        stack = [u.pop(0)]
        while u:
            stack.append(u.pop(0))
            if len(stack) >= 2 and stack[-2:] == ['(',')']:
                stack.pop()
                stack.pop()
                
        return len(stack) == 0
            
    # 두 균형잡힌 문자열로 분리하는 함수        
    def recursion(p):
        if not p:
            return ""
        
        left,right = 0,0
        
        for i,char in enumerate(p):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                u = p[:i+1]
                v = p[i+1:]
                
                # u가 올바른 문자열이라면 v를 다시 반복
                if is_valid(u):
                    return u + recursion(v)
                # u가 올바른 문자열이 아니라면
                else:
                    # 제일 앞에 '('를 추가해서 다시 재귀적으로 v추가
                    # 재귀 끝나고 마지막에 ')'를 다시 붙여
                    # u 첫번째와 마지막 제거, 나머지 문자열 괄호 방향 뒤집어서 뒤에 붙여
                    return '('+ recursion(v) + ')' + reverse(u[1:-1])
    
    
    answer = recursion(p)
    
    return answer