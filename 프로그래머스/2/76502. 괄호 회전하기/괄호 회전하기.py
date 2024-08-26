from collections import deque
def solution(s):
    answer = 0
    ds = deque(s)
    # print(ds)
    
    for i in range(len(s)):
        temlist = []
        # print(ds)
        for char in ds:
            temlist.append(char)
            
            if len(temlist) > 1:
                if temlist[-2:] == ['[',']'] or temlist[-2:] == ['(',')'] or temlist[-2:] == ['{','}']:
                    del temlist[-2:]
        #print(temlist)
        if len(temlist) == 0 :
            answer += 1
        ds.rotate(-1)
        
    return answer