# 염색체 # 실버3 # 문자열
# 규칙 만족하는지 검사!!!!
import re

def infecttion(case):
    pattern = r'^[ABCDEF]?A+F+C+[ABCDEF]?$'
    return bool(re.fullmatch(pattern,case))

t = int(input())

for i in range(t):
    case = input()
    if infecttion(case):
        print('Infected!')
    else:
        print('Good')