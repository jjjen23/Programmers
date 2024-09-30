# 구조 이해하기!!!!!!!!1
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)    
    
    for i in range(len(numbers)):
        
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
            
        stack.append(i) 
        
    return answer

"""
from collections import deque

def solution(numbers):
    answer = []
    
    numbers = deque(numbers)
    
    while numbers:
        tem = numbers.popleft()
        
        flag = True
        
        for i in numbers:
            if tem < i :
                answer.append(i)
                flag = False
                break
                
        if flag == True:
            answer.append(-1)
        
        
    return answer
"""