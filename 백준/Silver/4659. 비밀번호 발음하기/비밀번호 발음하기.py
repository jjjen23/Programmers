# 비밀번호 발음하기 # 실버 5 # 문자열 # 구현
import re
"""
1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

조건을 만족 시 acceptable
정규표현식이 편하려나....

"""
def test1(case):
    # 글자에 모음이 존재하면 True
    pattern1 = r'[aeiou]'
    # 모음이 3번 반복되거나 자음이 3번 반복되는 경우 True
    pattern2 = r'[aeiou]{3}|[^aeiou]{3}' #모음 3개 연속 or 모음 아닌게 오는지 체크
    # 조건 3: 같은 글자 두 번 연속 금지, 단 "ee"와 "oo"는 예외
    #  ee,oo는 문자열에 없고 나머지 문자열이 2회 반복되는 경우 True
    pattern3 = r'([a-df-np-z])\1'

    if re.search(pattern1,case) and not re.search(pattern2,case) and not re.search(pattern3,case):
        return print(f'<{case}> is acceptable.')
    else:
        return print(f'<{case}> is not acceptable.')


while True:
    testPw = input()
    if testPw == 'end':
        break
    else:
        test1(testPw)
