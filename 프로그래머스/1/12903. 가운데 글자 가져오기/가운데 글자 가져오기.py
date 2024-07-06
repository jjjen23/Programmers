import math

def solution(s):
    s = list(s)
    s_len = len(s)
    tem = (s_len+1) / 2  #중앙값 구하기
    answer = ''
    
    #글자수가 짝수일 때
    if s_len % 2 == 0:
        index1 = int(math.floor(tem))-1
        index2 = int(math.ceil(tem))-1
        answer = s[index1]+s[index2]
    #홀수 일 때
    else:
        index1 = int(tem-1)
        answer = s[index1]
        
    
    return answer