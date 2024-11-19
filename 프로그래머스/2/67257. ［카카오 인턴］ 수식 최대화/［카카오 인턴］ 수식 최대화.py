from collections import deque
from itertools import permutations
import re

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
    
    
    for per in permutations(후보,len(후보)):
        expression = deque(splitList)
        
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

            expression = mutical
            # print(expression,oper)      
        answer.append(abs(int(expression[0])))
    
    return max(answer)
