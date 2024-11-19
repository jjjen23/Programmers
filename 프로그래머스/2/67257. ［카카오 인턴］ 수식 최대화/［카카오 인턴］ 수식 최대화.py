from collections import deque
from itertools import permutations
import re

# 최대 세 가지 연산
def muti(oper1,oper2):
    return oper1*oper2
def summm(oper1,oper2):
    return oper1+oper2
def sub(oper1,oper2):
    return oper1-oper2

def solution(expression):
    answer = []
    후보 = re.findall(r'[\-\*\+]',expression)
    후보 = set(후보)
    # print(후보)
    # 절댓값으로 계산함 -> 가장 큰 금액 반환
    splitList = re.findall(r'\d+|[\-\*\+]',expression)
    # print(splitList)
    
    # 연산자에 따라 우선 순위 순열 생성
    for per in permutations(후보,len(후보)):
        expression = deque(splitList)
        
        # 우선순위 대로 계산
        for oper in per:
            mutical = deque()

            while expression:
                tem = expression.popleft()

                if tem == oper:
                    oper1 = int(mutical.pop())
                    oper2 = int(expression.popleft())

                    if oper == '*':
                        new = muti(oper1,oper2)
                    elif oper == '+':
                        new = summm(oper1,oper2)
                    elif oper == '-':
                        new = sub(oper1,oper2)
                    mutical.append(str(new))

                else: mutical.append(tem)

            expression = mutical # 계산된 것을 갱신
            # print(expression,oper)      
        answer.append(abs(int(expression[0]))) # 조합별 계산 결과 저장(절대값으로)
    
    # 가장 큰 값 출력
    return max(answer)
