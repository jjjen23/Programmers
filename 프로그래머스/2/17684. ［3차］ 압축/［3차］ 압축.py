import string

def solution(msg):
    answer = []
    upper = [i for i in string.ascii_uppercase]
    
    dict1 = {}
    for i in range(len(upper)):
        dict1[upper[i]] = i+1 
    
    while True:
        
        # 다음 글자가 없는 경우 처리(마지막 처리구문이고 종료구문이됨)
        if msg in dict1:
            answer.append(dict1[msg])
            break
        
        
        for i in range(1,len(msg)+1):
            if msg[0:i] not in dict1:
                answer.append(dict1[msg[0:i-1]])
                dict1[msg[0:i]] = len(dict1)+1
                msg = msg[i-1:]
                break

        
    return answer

"""
def solution(msg):
    answer = []
    upper = [i for i in string.ascii_uppercase]
    
    dict1 = {}
    for i in range(len(upper)):
        dict1[upper[i]] = i+1 
    

    msg = list(msg)
    w = msg.pop(0)
    
    while msg:
        c = msg.pop(0)
        tem = w
        
        while tem+c in dict1:
            tem += c
            if msg:
                c = msg.pop(0)
            else:
                c = ''
                break
        print(tem)
        answer.append(dict1[tem])
        dict1[tem+c] = len(dict1) + 1
        
        w = c
     # 마지막에 남아 있는 w를 결과에 추가
    if w:
        answer.append(dict1[w])

        
    return answer
"""